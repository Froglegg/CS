from tabulate import tabulate
from simple_term_menu import TerminalMenu

salesDict = {
    "Clarence Carson": {
        "Name": "Clarence Carson",
        "Salary": 250.00,
        "Gross sales": 1000.00,
        "Rate": 3.2,
    },
    "Daphne Danvers": {
        "Name": "Daphne Danvers",
        "Salary": 100.00,
        "Gross sales": 6000.00,
        "Rate": 6.5

    },
    "Julia Jefferson": {
        "Name": "Julia Jefferson",
        "Salary": 100.00,
        "Gross sales": 4000.00,
        "Rate": 3.2

    },
    "Randolph Reeds": {
        "Name": "Randolph Reeds",
        "Salary": 250.00,
        "Gross sales": 2000.00,
        "Rate": 6.5

    },
    "Sabrina Sanders": {
        "Name": "Sabrina Sanders",
        "Salary": 250.00,
        "Gross sales": 3000.00,
        "Rate": 3.2

    }
}


def buildTableFromDict(dict, headers):

    data = [[j for j in i.values()] for i in dict.values()]

    table = tabulate(data, headers=headers,
                     tablefmt="github", numalign="left")
    return table


def calculateAndSetCommisionAndIncome(salesperson, dict):
    rate = dict[salesperson]["Rate"]
    grossSales = dict[salesperson]["Gross sales"]
    commission = rate * grossSales
    grossIncome = commission + grossSales
    dict[salesperson].update(
        {"Commission": round(commission, 2), "Gross Income": round(grossIncome, 2)})
    return commission


def selectAndViewSalesPerson(dict):
    options = list(dict.keys())
    entry = TerminalMenu(
        options, title="\nWho would you like to inspect?").show()

    salesperson = dict[options[entry]]

    for item in salesperson.items():
        print(f"{item[0]} : {item[1]}")


def main():
    global salesDict
    """
        •	computes the commission amount of each salesperson by multiplying their gross sales and their commission rate

        •	computes the gross income of each salesperson by adding their base salary to their commission amount

        •	generates a report that lists the total commission amounts of all of the salespersons

        •	allows the program user to query a particular salesperson to obtain their respective data values
    """
    print("\nHello and welcome to the commissions calculator! \n")
    while True:
        entry = TerminalMenu(["View Salespersons Table", "Calculate total commisions and salary",
                              "View particular salesperson", "Exit"], title="\nWhat would you like to do?").show()

        if entry == 0:
            print(buildTableFromDict(salesDict, [
                  "Name", "Salary", "Gross Sales", "Rate", "Commission", "Gross Income"]))

        elif entry == 1:
            for salesperson in salesDict.keys():
                calculateAndSetCommisionAndIncome(salesperson, salesDict)
            print(buildTableFromDict(salesDict,  [
                  "Name", "Salary", "Gross Sales", "Rate", "Commission", "Gross Income"]))

        elif entry == 2:
            selectAndViewSalesPerson(salesDict)

        else:
            print("Goodbye!")
            exit()


if __name__ == "__main__":
    main()
