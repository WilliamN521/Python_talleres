"""
1 Exercise
----------

Draw R2D2
    --------    
   /   ()   \   
 _|__________|_ 
| |   =====  | |
|_|     o    |_|
 ||     o    || 
 ||_____ ____|| 
|~ \________/~ |
/=\    /=\   /=\
[ ]    [ ]   [ ]

"""
# variables to store each character/symbol
space = " "
dash = "-"
underscore = "_"
parallel = "|"
parenthesis = "("
parenthesis_2 = ")"
equal = "="
o = "o"
slash = "/"
backslash = "\\"
bracket = "["
bracket_2 = "]"
simbol = "~"
point = "."
numeral = "#"

# R2D2
print(f"\n{space*6}R2D2")
print(f"{space*4}{dash*8}")
print(f"{space*3}{slash}{space*3}{parenthesis}{parenthesis_2}{space*3}{backslash}")
print(f"{space}{underscore}{parallel}{underscore*10}{parallel}{underscore}")
print(f"{parallel}{space}{parallel}{space*3}{equal*5}{space*2}{parallel}{space}{parallel}")
print(f"{parallel}{underscore}{parallel}{space*5}{o}{space*4}{parallel}{underscore}{parallel}")
print(f"{space}{parallel*2}{space*5}{o}{space*4}{parallel*2}")
print(f"{space}{parallel*2}{underscore*5}{space}{underscore*4}{parallel*2}")
print(f"{parallel}{simbol}{space}{backslash}{underscore*8}{slash}{simbol}{space}{parallel}")
print(f"{slash}{equal}{backslash}{space*4}{slash}{equal}{backslash}{space*3}{slash}{equal}{backslash}")
print(f"{bracket}{space}{bracket_2}{space*4}{bracket}{space}{bracket_2}{space*3}{bracket}{space}{bracket_2}")

"""
Draw C-3PO
   /~\
  |oo )
  _\=/_
 /  _  \
//|/.\|\\
\\ \_/  ||
 \|\ /| ||
 # _ _/  #
  | | |
  | | |
  []|[]
  | | |
 / ] [ \
"""
# C-3PO
print(f"\n\n{space*2}C-3PO")
print(f"{space*3}{slash}{simbol}{backslash}")
print(f"{space*2}{parallel}{o*2}{space}{parenthesis_2}")
print(f"{space*2}{underscore}{backslash}{equal}{slash}{underscore}")
print(f"{space}{slash}{space*2}{underscore}{space*2}{backslash}")
print(f"{slash*2}{parallel}{slash}{point}{backslash}{parallel}{backslash*2}")
print(f"{backslash*2}{space}{backslash}{underscore}{slash}{space*2}{parallel*2}")
print(f"{space}{backslash}{parallel}{backslash}{space}{slash}{parallel}{space}{parallel*2}")
print(f"{space}{numeral}{space}{underscore}{space}{underscore}{slash}{space*2}{numeral}")
print(f"{space*2}{parallel}{space}{parallel}{space}{parallel}")
print(f"{space*2}{parallel}{space}{parallel}{space}{parallel}")
print(f"{space*2}{bracket}{bracket_2}{parallel}{bracket}{bracket_2}")
print(f"{space*2}{parallel}{space}{parallel}{space}{parallel}")
print(f"{space}{slash}{space}{bracket_2}{space}{bracket}{space}{backslash}")
