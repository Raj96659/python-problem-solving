# Write a Python program to convert kilometers to miles.

enter_km = int(input("Enter the kilometers : "))

con_factor = 0.6213

to_miles = enter_km * con_factor

print(f"{enter_km} km is equal to {to_miles:.2f} miles")
