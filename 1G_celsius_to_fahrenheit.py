#  Write a Python program to convert Celsius to Fahrenheit.

temp_c = int(input('Enter the temperature in celsius : '))

to_fahrenheit = (temp_c * 9/5) + 32

print(f"{temp_c}°C is equal to {to_fahrenheit:.2f}°F")
