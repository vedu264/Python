print("Welcome to the tip calculator")

bill = input("What was the total bill? $")
tip = input("What percentage tip would you like to give? 10.12, or 15?")

z = input("How many people to split the bill?")

tip_as_percent = int(tip)/100 * float(bill)
final_tip = float(tip_as_percent) + float(bill)
tipped = float(final_tip) / int(z)

print(f"Each person should pay: ${round(tipped,2)}")