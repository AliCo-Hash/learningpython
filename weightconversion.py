inputWeight = float(input("Please enter your weight\n"))
weightUnit = input("(K)g or (L)bs: ")

if weightUnit.upper() == "K":
  print(f"Weight in Lbs: {inputWeight * 2.20462}")
elif weightUnit.upper() == "L":
  print(f"Weight in Kgs: {inputWeight * 0.453592}")
else:
  print("Please enter a valid unit")