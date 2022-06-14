"""
Ejercicio 5
-----------

Se debe crear un programa que dada luna longitud en cuadros
(mayor a cero), genere un tablero, como en la siguiente imagen (Es
un tablero con una longitud de 8x8

   ***   ***   ***
***   ***   ***   
   ***   ***   ***
***   ***   ***   
   ***   ***   ***
***   ***   ***   
"""

length = int(input("enter then length of the chessboard: "))
print()

for row in range(length):
  for col in range(length):
    if (row+col) % 2 == 0:
      print(" "*3, end="")
    else:
      print("*"*3, end="")
  print()