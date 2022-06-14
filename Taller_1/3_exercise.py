"""
3 Excercise
-----------

Degrees fahrenheit to centigrades
"""

# capture data
fahrenheit = float(input("\nenter fahrenheit grades: "))
# Transformation and rounding of decimals
centigrades = round((fahrenheit - 32)*(5/9),3)
# Display on screen the results
print(f"\nFahrenheit   ->   Centrigades")
print(f"{fahrenheit} °F      =   {centigrades} °C")