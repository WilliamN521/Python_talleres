""" 
2 Exercise
----------

Data capture of all users
"""
# Personal information user 1
print(f"\nUser 1")
user1_name_lastname = input("enter your name and last name: ")
user1_ocupation = input("enter your occupation: ")
user1_age = int(input("enter your age: "))
user1_city = input("enter your city: ")
user1_contact_number = int(input("enter your contact number: "))
user1_email = input("enter your email: ")

# Personal information user 2
print(f"\nUser 2")
user2_name_lastname = input("enter your name and last name: ")
user2_ocupation = input("enter your occupation: ")
user2_age = int(input("enter your age: "))
user2_city = input("enter your city: ")
user2_contact_number = int(input("enter your contact number: "))
user2_email = input("enter your email: ")

# Personal information user 3
print(f"\nUser 3")
user3_name_lastname = input("enter your name and last name: ")
user3_ocupation = input("enter your occupation: ")
user3_age = int(input("enter your age: "))
user3_city = input("enter your city: ")
user3_contact_number = int(input("enter your contact number: "))
user3_email = input("enter your email: ")

# Store of each user's information in an immutable structure
user1 = (user1_name_lastname, user1_ocupation, user1_age, user1_city, user1_contact_number, user1_email)

user2 = (user2_name_lastname, user2_ocupation, user2_age, user2_city, user2_contact_number, user2_email)

user3 = (user3_name_lastname, user3_ocupation, user3_age, user3_city, user3_contact_number, user3_email)

# Store the captured information in a mutable structure
users = [list(user1), list(user2), list(user3)]

# Display on screen the information of each user
print(f"\n\n\tUsers Personal Information\n\nUser 1")
# name and lastname
print(f"name and last name:\t{users[0][0]} \
    \noccupation:\t\t{users[0][1]} \
    \nage:\t\t\t{users[0][2]} \
    \ncity:\t\t\t{users[0][3]} \
    \ncontact number:\t\t{users[0][4]} \
    \nemail:\t\t\t{users[0][5]}")
# user 2
print(f"\nUser 2\nname and last name:\t{users[1][0]} \
    \noccupation:\t\t{users[1][1]} \
    \nage:\t\t\t{users[1][2]} \
    \ncity:\t\t\t{users[1][3]} \
    \ncontact number:\t\t{users[1][4]} \
    \nemail:\t\t\t{users[1][5]}")
# user 3
print(f"\nUser 3\nname and last name:\t{users[2][0]} \
    \noccupation:\t\t{users[2][1]} \
    \nage:\t\t\t{users[2][2]} \
    \ncity:\t\t\t{users[2][3]} \
    \ncontact number:\t\t{users[2][4]} \
    \nemail:\t\t\t{users[2][5]}")
