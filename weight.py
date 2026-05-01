weight = float(input("enter your weight:"))
measuring_unit = input("k for kg and l for pounds")

if (measuring_unit == 'k'):
    print(f"{weight}kg " "in pounds is ",weight * 2.205)
elif(measuring_unit == 'l'):
    print(f"{weight}lb " "in kg is ",weight / 2.205)
else:
    print("Invalid input")

