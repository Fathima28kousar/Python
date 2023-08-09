unit = int(input("Enter the units: "))
if unit<=100:
    amount = 0
if unit>100 and unit<200:
    amount = (unit-100)*5
if unit>200:
    amount = 500 + (unit-200)*10
print("Amount to pay:",amount)    