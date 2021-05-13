print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? "))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))
bill_per_person = bill * (1 + tip / 100) / people
rounded_bill = "{:.2f}".format(round(bill_per_person, 2))
print(f"Each person should pay: ${rounded_bill}")
