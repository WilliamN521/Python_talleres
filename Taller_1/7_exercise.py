"""
7 Exercise
----------

Transform the text with the methods and functions of strings and lists

"""
text = "thor lanzó su martillo#flash ha fallado por un pie! -gritó Loki \
Laufeyson#dos pies -le corrigió Hulk#flash menea la cabeza como \
disgustado…  -agrega el comentarista"

# row 1 capitalization and replacement
final_row_1 = text[:23].capitalize().replace("#","...")

# row 2 split, add the simbol "-", capitalization, replacement and join
row_2 = text[23:74].split()
simbol = "-"
row_2.insert(0,simbol)
row_2[1] = row_2[1].capitalize()
row_2[-1] = row_2[-1].replace("#",".")
final_row_2 = " ".join(row_2)
# split the row to add character in specefic part
final_row_2 = final_row_2[:2] + "¡" + final_row_2[2:]

# row 3 split, add the simbol "-", capitalization, replacement and join
row_3 = text[74:101].split()
row_3.insert(0,simbol)
row_3[1] = row_3[1].capitalize()
row_3[3] = row_3[3].replace("-","")
row_3[5] = row_3[5].replace("#",".")
final_row_3 = " ".join(row_3)

# row 4 split, add the simbol "-", capitalization, join and add the end "."
row_4 = text[101:164].split()
row_4.insert(0,simbol)
row_4[1] = row_4[1].capitalize()
final_row_4 = " ".join(row_4)
final_row_4 = final_row_4[:] + "."

# show the results
print(f"\nOriginal Text: \n\n{text}")
print(f"\nFinal Text: \n\n{final_row_1}\n{final_row_2}\n{final_row_3}\n{final_row_4}")