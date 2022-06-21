
"""
2 Exercise
----------
Encode and decode a message with numbers

"""


def menu():
    """sumary_line
    
    Returns:
        str : menu execution with options and functions used
    """
    
    while True:
        try:
            print(f"\n\t\tMenu\n")
            print(f"1) Encode Message\n2) Decode Message\n3) Exit")
            option = int(input("Enter an option: "))
            if option == 1:
                text = input("Enter the message to encode: ")
                value = coder(text)
                print("¡ Coded Message !")
            elif option == 2:
                print("\nDecoding Message.....")
                print(decoder(coder(value)))
            elif option == 3:
                print("Closing execution...\n")
                break
            else:
                print("\nError: Enter a correct option.")
        except ValueError:
            print("\nError: Enter only numbers.")
        except UnboundLocalError:
            print("\nError: First, encoded a message.")
            
            
    
def coder(text):
    """Encodes the message

    Args:
        text (str): text string representing the message to encode

    Returns:
        str : encoded text string, with the respective values
    """
    conversion = {1: 9, 2: 8, 3: 7, 4: 6, 5: 0}
    lista = list(text)

    for i in range(len(lista)):
        e = lista[i]
        if e.isdigit():
            for k, v in conversion.items():
                if int(e) == k:
                    lista[i] = str(v)
                elif int(e) == v:
                    lista[i] = str(k)
    result_text = ''.join(lista)
    return result_text


def decoder(text):
    """Decode the message using the previous encoder function
    
    Args:
        text (str): text string representing the coded message

    Returns:
        str : decoded text string, with the respective values
    """
    return coder(text)

# Menu Execution 
menu()
