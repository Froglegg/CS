from trans import bank_list

my_list = bank_list()
total = 0.0

my_list.append({"2020-05-13": -1000})

print("\nRichard Hayes Crowley CSC_157_lab_06\n")
for item in my_list:
    for key, value in item.items():
        print(f"Date: {key} Bal: ${round(value,2):.2f}")

        total += value
print(f"\nTotal balance: ${round(total,2):.2f}")
