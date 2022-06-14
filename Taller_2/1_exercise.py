"""
Ejercicio 1
-----------
El capitán del barco pirata Thousand Sunny

"""

indication = "¡Ahay! capitán,"
direction_list = ["Babor","Estribor", "Proa", "Popa"]

while True:
    creature = input("\nCaptain.. what is the creature?: ")
    
    if creature == "stop":
        print("Captain, it is the end.")
        break
    else:
        if creature != "kraken" and creature != "sirenas" and creature != "ballena" and creature != "hipocampo" and creature != "macaraprono" and creature != "pulpo" and creature != "levitantes" and creature != "hidras":
            print("other specie please..")
            continue
        else:
            direction = input("And the direction?: ").capitalize()
            # Kraken
            if creature.capitalize() == "Kraken":
                if direction == direction_list[0]:
                    print(f"{indication} un {creature.capitalize()} a {direction.lower()}\n ")
                elif direction == direction_list[1]:
                    print(f"{indication} un {creature.capitalize()} a {direction.lower()}\n")
                elif direction == direction_list[2]:
                    print(f"{indication} un {creature.capitalize()} por la {direction.lower()}\n")
                elif direction == direction_list[3]:
                    print(f"{indication} un {creature.capitalize()} por la {direction.lower()}\n")
                else:
                    print(f"The direction is incorrect.")
            # Sirenas
            elif creature.capitalize() == "Sirenas":
                if direction == direction_list[0]:
                    print(f"{indication} unas {creature.capitalize()} a {direction.lower()}\n ")
                elif direction == direction_list[1]:
                    print(f"{indication} unas {creature.capitalize()} a {direction.lower()}\n")
                elif direction == direction_list[2]:
                    print(f"{indication} unas {creature.capitalize()} por la {direction.lower()}\n")
                elif direction == direction_list[3]:
                    print(f"{indication} unas {creature.capitalize()} por la {direction.lower()}\n")
                print(f"The direction is incorrect.")
            # Ballena
            elif creature.capitalize() == "Ballena":
                if direction == direction_list[0]:
                    print(f"{indication} una {creature.capitalize()} a {direction.lower()}\n ")
                elif direction == direction_list[1]:
                    print(f"{indication} una {creature.capitalize()} a {direction.lower()}\n")
                elif direction == direction_list[2]:
                    print(f"{indication} una {creature.capitalize()} por la {direction.lower()}\n")
                elif direction == direction_list[3]:
                    print(f"{indication} una {creature.capitalize()} por la {direction.lower()}\n")
                else:
                    print(f"The direction is incorrect.")
            # Hipocampo
            elif creature.capitalize() == "Hipocampo":
                if direction == direction_list[0]:
                    print(f"{indication} un {creature.capitalize()} a {direction.lower()}\n ")
                elif direction == direction_list[1]:
                    print(f"{indication} un {creature.capitalize()} a {direction.lower()}\n")
                elif direction == direction_list[2]:
                    print(f"{indication} un {creature.capitalize()} por la {direction.lower()}\n")
                elif direction == direction_list[3]:
                    print(f"{indication} un {creature.capitalize()} por la {direction.lower()}\n")
                else:
                    print("The direction is incorrect.")
            # Macaraprono
            elif creature.capitalize() == "Macaraprono":
                if direction == direction_list[0]:
                    print(f"{indication} una {creature.capitalize()} a {direction.lower()}\n ")
                elif direction == direction_list[1]:
                    print(f"{indication} una {creature.capitalize()} a {direction.lower()}\n")
                elif direction == direction_list[2]:
                    print(f"{indication} una {creature.capitalize()} por la {direction.lower()}\n")
                elif direction == direction_list[3]:
                    print(f"{indication} una {creature.capitalize()} por la {direction.lower()}\n")
                else:
                    print("The direction is incorrect")
            # Pulpo
            elif creature.capitalize() == "Pulpo":
                if direction == direction_list[0]:
                    print(f"{indication} un {creature.capitalize()} a {direction.lower()}\n ")
                elif direction == direction_list[1]:
                    print(f"{indication} un {creature.capitalize()} a {direction.lower()}\n")
                elif direction == direction_list[2]:
                    print(f"{indication} un {creature.capitalize()} por la {direction.lower()}\n")
                elif direction == direction_list[3]:
                    print(f"{indication} un {creature.capitalize()} por la {direction.lower()}\n")
                else:
                    print("The direction is incorrect.")
            # Levitantes
            elif creature.capitalize() == "Levitantes":
                if direction == direction_list[0]:
                    print(f"{indication} unos {creature.capitalize()} a {direction.lower()}\n ")
                elif direction == direction_list[1]:
                    print(f"{indication} unos {creature.capitalize()} a {direction.lower()}\n")
                elif direction == direction_list[2]:
                    print(f"{indication} unos {creature.capitalize()} por la {direction.lower()}\n")
                elif direction == direction_list[3]:
                    print(f"{indication} unos {creature.capitalize()} por la {direction.lower()}\n")
                else:
                    print("The direction is incorrect.")
            # Hidras
            elif creature.capitalize() == "Hidras":
                if direction == direction_list[0]:
                    print(f"{indication} unas {creature.capitalize()} a {direction.lower()}\n ")
                elif direction == direction_list[1]:
                    print(f"{indication} unas {creature.capitalize()} a {direction.lower()}\n")
                elif direction == direction_list[2]:
                    print(f"{indication} unas {creature.capitalize()} por la {direction.lower()}\n")
                elif direction == direction_list[3]:
                    print(f"{indication} unas {creature.capitalize()} por la {direction.lower()}\n")
                else:
                    print("The direction is incorrect.")
    