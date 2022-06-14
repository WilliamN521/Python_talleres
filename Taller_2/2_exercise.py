"""
Ejercicio 2
-----------

Radares
v = x/t
v: velocidad
x: posición - distancia
t: tiempo
"""

distance = float(input("enter the total distance in (meters): "))
time = int(input("enter the time (in seconds): "))

speed = (distance*3600)/(time*1000)

if speed <= 0:
    print("\nNo penalty")
elif speed >= 1 and speed <= 20:
    print(f"\nCalled to attention for low speed: {speed}km/h")
elif speed >= 21 and speed <= 60:
    print(f"\nNormal: {speed}km/h")
elif speed >= 61 and speed <= 80:
    print(f"\nCalled to attention for high speed: {speed}km/h")
elif speed >= 81 and speed <= 120:
    alcohol = int(input("enter the mg alcohol: "))
    if alcohol < 20:
        print(f"\nPenalty Tipe II and immobilization of the vehicle in: {speed}km/h")
    elif alcohol >= 20 and alcohol <= 39:
        print(f"\nPenalty Tipe I for: {speed}km/h and \
        \nSuspension of the driver's license between six (6) and twelve (12) months.")
    elif alcohol >= 40 and alcohol <= 99:
        print(f"\nPenalty Tipe I for: {speed}km/h and \
        \nSuspension of the driver's license between one (1) and three (3) years.")
    elif alcohol >= 100 and alcohol <= 149:
        print(f"\nPenalty Tipe I for: {speed}km/h and \
        \nSuspension of the driver's license between three (3) and five (5) years. \
        \nAnd the obligation to take a course on awareness, knowledge and consequences \
        of alcohol and drug addiction in authorized rehabilitation centers, for a minimum of forty (40) days. ")
    else:
        print(f"\nPenalty Tipe I for: {speed}km/h and \
        \nSuspension of the driver's license between five (5) and ten (10) years. \
        \nAnd the obligation to take a course on awareness, knowledge and consequences \
        of alcohol and drug addiction in authorized rehabilitation centers, for a minimum of eighty (80) days. ")
else: 
    alcohol = int(input("enter the mg alcohol: "))
    if alcohol < 20:
        print(f"\nPenalty Tipe II and immobilization of the vehicle in: {speed}km/h")
    elif alcohol >= 20 and alcohol <= 39:
        print(f"\nPenalty Tipe II and immobilization of the vehicle in: {speed}km/h and \
        \nSuspension of the driver's license between six (6) and twelve (12) months.")
    elif alcohol >= 40 and alcohol <= 99:
        print(f"\nPenalty Tipe II and immobilization of the vehicle in: {speed}km/h and \
        \nSuspension of the driver's license between one (1) and three (3) years.")
    elif alcohol >= 100 and alcohol <= 149:
        print(f"\nPenalty Tipe II and immobilization of the vehicle in: {speed}km/h and \
        \nSuspension of the driver's license between three (3) and five (5) years. \
        \nAnd the obligation to take a course on awareness, knowledge and consequences \
        \nof alcohol and drug addiction in authorized rehabilitation centers, for a minimum of forty (40) days. ")
    else:
        print(f"\nPenalty Tipe II and immobilization of the vehicle in: {speed}km/h and \
        \nSuspension of the driver's license between five (5) and ten (10) years. \
        \nAnd the obligation to take a course on awareness, knowledge and consequences \
        \nof alcohol and drug addiction in authorized rehabilitation centers, for a minimum of eighty (80) days. ")
