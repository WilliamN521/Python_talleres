"""
Ejercicio 3
-----------

Fórmula de Galileo Galilei 

d = v ∗ t ± (1/2)) ∗ g ∗ 𝑡2 , donde:

"""

height = int(input("enter de building height (meters): "))
gravity = 9.8
second = 0
# distance accumulated
covered_distance = 0

if height > 0:
    while True:
        distance = round((0.5 * gravity * (second**2)),2)
        covered_distance += distance
        if covered_distance <= height:
            print(f"Time: {second} (s) \tCovered Distance: {covered_distance} (m)")
        else:
            break
        second += 1
else:
    print("Height error, must be greater than 0")

 