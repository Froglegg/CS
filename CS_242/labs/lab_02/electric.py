# ---------------------------------------------------
# Richard Hayes Crowley
# CSC_242
# ---------------------------------------------------

def getCustomerData():

    custName = input("please enter the Customer Name: ")
    custID = int(input("please enter the Customer Number: "))
    custAddress = input("please enter the Customer's address: ")
    kwhUsed = int(input("please enter Kilowatt - Hours ( KWH ) used: "))
    pastDue = float(input("please enter the amount past due: "))

    return {"custName": custName, "custID": custID, "custAddress": custAddress, "kwhUsed": kwhUsed, "pastDue": pastDue}

# ---------------------------------------------------


def calculateElecticBill(kwhUsed, pastDue):

    amt = 0
    penalty = 0
    total = 0
    surcharge = 0

    if kwhUsed <= 125:
        amt = .10 * kwhUsed
    elif kwhUsed <= 325:
        amt = 12.50 + (0.09 * kwhUsed)
    elif kwhUsed <= 500:
        amt = 30.60 + (0.08 * kwhUsed)
    else:
        amt = 42.60 + (0.06 * kwhUsed)

    # if If the electricity bill, prior to any amount past due, exceeds $ 300 then a surcharge of 12 % will be charged.
    if amt > 300:
        surcharge = amt * 0.12

    penalty = pastDue * 0.025
    total = amt + pastDue + penalty + surcharge

    return {"total": total, "penalty": penalty, "pastDue": pastDue, "surcharge": surcharge}

# ---------------------------------------------------


# call the functions
customer = getCustomerData()
bill = calculateElecticBill(customer["kwhUsed"], customer["pastDue"])

# destructure dict values
custId, custName, custAddress, kwhUsed = customer["custID"], customer[
    "custName"], customer["custAddress"], customer["kwhUsed"],
total, penalty, pastDue, surcharge = f"{round(bill['total'],2):0.2f}", f"{round(bill['penalty'],2):0.2f}", f"{round(bill['pastDue'],2):0.2f}", f"{round(bill['surcharge'],2):0.2f}"

# ---------------------------------------------------
# display the Electricity Bill Summary
print("Electricity Bill")
print("\n****************\n")
print("Customer ID Number\t", custId)
print("Customer Name\t", custName)
print("Customer Address\t", custAddress)
print("\n")
print(f"KWH Kilowatt - Hours ( KWH ) used\t {kwhUsed} KWH")
print(
    f"Surcharge (if bill is greater than $300, add 12% surcharge)\t {surcharge}")
print(f"Amount past due\t {pastDue}")
print(f"Penalty\t {penalty}")
print(f"Total owed\t {total}")

x = 5
if (x > 4 and x < 10):
    print("success")
if (4 < x < 10):
    print("success")
