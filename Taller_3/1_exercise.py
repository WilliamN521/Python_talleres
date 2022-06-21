"""
1 Exercise
----------
Get data about a person and write the information in a txt file
"""

import os

"""
- Set the path file
- Open, read and append file mode
- f = required_data.txt 
- n = new_file.txt
"""
path = rf"{os.getcwd()}"
f = open(rf"{path}\required_data.txt", "r", encoding="utf-8")
n = open(rf"{path}\new_file.txt", "a+", encoding="utf-8")

# List to store the information items
personal_data = [
    "Full name*:", "Age*:", "Height*:", "Weight*:", "Blood-type*:", 
    "Illnesses*:","Profession*:", "Home country*:", "Home city*:", 
    "Address:", "Contact number:", "Emergency contact*:", "Email*:"]

def personal():
    """Store input data information 
    
    Returns:
    list : Get the personal data information and return data stored in a list
    """
    data_answers = []
    print("\nPlase, enter your\n")
    for i in range(len(personal_data)):
        text = input(f"{personal_data[i]} ")
        data_answers.append(text)
    return data_answers

def personal_data_file():
    """Use personal data answers and aggregate the information
        appending it with the mother data 
    
    Returns:
    list : if attribute doesn't have *, put unknown
    """
    answers = personal()
    text = mother_data_file()
    # index to range 
    j = 0
    # Start in the line 4 because from this number line begins personal data and ends in 17 line
    for i in range(4, 17):
        evaluate = text[i].rstrip()
        if evaluate == personal_data[j]:
            if evaluate[-2] == "*":
                text[i] = text[i].rstrip() + " " + answers[j]
            else:
                text[i] = text[i].rstrip() + " unknown"
        j+=1
    return text

# List to store the mother and father information items
mother_father_data = [
    "Full name*:", "Age*:", "Blood-type*:", "Illnesses*:",
    "Profession:", "Home country*:", "Home city*:", 
    "Address*:", "Contact number*:", "Email:"]

def mother():
    """Store input data information 
    
    Returns:
    list : Get the mother data information and return data stored in a list
    """
    data_answers = []
    print("\nPlase, enter your Mother's\n")
    for i in range(len(mother_father_data)):
        text = input(f"{mother_father_data[i]} ")
        data_answers.append(text)
    return data_answers

def mother_data_file():
    """Use mother data answers and aggregate the information
        appending it with the father data 
    
    Returns:
    list : if attribute doesn't have *, put unknown
    """
    answers = mother()
    text = father_data_file()
    j = 0
    # Start in the line 23 because from this number line begins mother data and ends in 33 line
    for i in range(23, 33):
        evaluate = text[i].strip()
        if evaluate == mother_father_data[j]:
            if evaluate[-2] == "*":
                text[i] = text[i].rstrip() + " " + answers[j]
            else:
                text[i] = text[i].rstrip() + " unknown"
        j+=1
    return text


def father():
    """Store input data information 
    
    Returns:
    list : Get the father data information and return data stored in a list
    """
    data_answers = []
    print("\nPlase, enter your Father's\n")
    for i in range(len(mother_father_data)):
        text = input(f"{mother_father_data[i]} ")
        data_answers.append(text)
    return data_answers

def father_data_file():
    """Use father data answers and aggregate the information
        appending it with the brother data 
    
    Returns:
    list : if attribute doesn't have *, put unknown
    """
    answers = father()
    text = brother_data_file()
    j = 0
    # Start in the line 35 because from this number line begins father data and ends in 45 line
    for i in range(35, 45):
        evaluate = text[i].strip()
        if evaluate == mother_father_data[j]:
            if evaluate[-2] == "*":
                text[i] = text[i].rstrip() + " " + answers[j]
            else:
                text[i] = text[i].rstrip() + " unknown"
        j+=1
    return text


# List to store the brother information items
brother_data = [
    "Full name*:", "Age*:", "Blood-type*:", "Illnesses*:",
    "Profession*:", "Home country:", "Home city:", 
    "Address:", "Contact number*:", "Email:"]

def brother():
    """Store input data information 
    
    Returns:
    list : Get the brother data information and return data stored in a list
    """
    data_answers = []
    print("\nPlase, enter your Brother's\n")
    for i in range(len(brother_data)):
        text = input(f"{brother_data[i]} ")
        data_answers.append(text)
    return data_answers

def brother_data_file():
    """Use brother data answers and aggregate the information
        appending it with the sister data 
    
    Returns:
    list : if attribute doesn't have *, put unknown
    """
    answers = brother()
    text = sister_data_file()
    j = 0
    # Start in the line 47 because from this number line begins personal data and ends in 57 line
    for i in range(47, 57):
        evaluate = text[i].strip()
        if evaluate == brother_data[j]:
            if evaluate[-2] == "*":
                text[i] = text[i].rstrip() + " " + answers[j]
            else:
                text[i] = text[i].rstrip() + " unknown"
        j+=1
    return text


# List to store the sister information items
sister_data = [
    "Full name*:", "Age*:", "Blood-type*:", "Illnesses*:",
    "Profession:", "Home country:", "Home city:", 
    "Address:", "Contact number*:", "Email:"]

def sister():
    """Store input data information 
    
    Returns:
    list : Get the sister data information and return data stored in a list
    """
    data_answers = []
    print("\nPlase, enter your Sister's\n")
    for i in range(len(sister_data)):
        text = input(f"{sister_data[i]} ")
        data_answers.append(text)
    return data_answers

def sister_data_file():
    """Use sister data answers and aggregate the information
        appending it with the file data 
    
    Returns:
    list : if attribute doesn't have *, put unknown
    """
    answers = sister()
    text = f.readlines()
    j = 0
    # Start in the line 59 because from this number line begins personal data and ends in 69 line
    for i in range(59, 69):
        evaluate = text[i].strip()
        if evaluate == sister_data[j]:
            if evaluate[-2] == "*":
                text[i] = text[i].rstrip() + " " + answers[j]
            else:
                text[i] = text[i].rstrip() + " unknown"
        j+=1
    f.close()
    return text

# join and write all data in txt new file
n.write('\n'.join(personal_data_file()))
n.close()

