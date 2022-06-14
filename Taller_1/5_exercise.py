"""
5 Exercise
----------

Capture of each note and its percentage
"""

# note 1 - percentage 1
note_1 = float(input("\nenter note 1: "))
percent_1 = float(input("enter percent of note 1: "))
# note 2 - percentage 2
note_2 = float(input("\nenter note 2: "))
percent_2 = float(input("enter percent of note 2: "))
# note 3 - percentage 3
note_3 = float(input("\nenter note 3: "))
percent_3 = float(input("enter percent of note 3: "))

# calculate the value of each note
n1 = note_1*(percent_1/100)
n2 = note_2*(percent_2/100)
n3 = note_3*(percent_3/100)

# note average and rounding of 2 decimals
average_score = round(((note_1+note_2+note_3)/3),2)
# final note and rounding of 2 decimals
final_note = round((n1+n2+n3),2)

# show de results
print(f"\nAverage score: {average_score} \n  Final score: {final_note}")