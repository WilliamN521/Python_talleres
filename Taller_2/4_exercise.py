"""
Ejercicio 4
------------

Personas por generación
"""

generation = int(input("enter a generation: "))


if generation >= 0:
    persons = 1
    for i in range(generation+1):
        if generation > 0:
            print(f"#Generation: {i}\t #Persons: {persons}")
            persons *= 2
        else:
            print(f"#Generation: {i}\t #Persons: {persons}")
else:
    print(f"Number of generation is incorrect")