# Richard Hayes Crowley
# 2/06/2021
# CSC_157_Lab_03

# Calculating BMI

def calculate_bmi(weight, height):
    msg = {
        "bmi": "",
        "weight": "normal",
        "message": ""
    }
    msg["bmi"] = round(weight * 703 / height**2, 1)
    if msg["bmi"] < 18.5:
        msg["weight"] = "underweight"
    elif msg["bmi"] > 25:
        msg["weight"] = "overweight"
    return msg


print('Richard Hayes Crowley\n2/06/2021\nCSC_157_Lab_03\n')
print("Body mass index (BMI) calculator")

while True:
    weight = float(input("\nPlease enter your weight (US pounds): "))
    height = float(input("Please enter your height (US inches): "))
    msg = calculate_bmi(weight, height)
    # print(msg["bmi"])
    print(f"Your BMI is: {msg['bmi']}\nYour weight is: {msg['weight']}")
    repeat = input("\nEnter 'y' to continue: ")
    if repeat != "y":
        break
