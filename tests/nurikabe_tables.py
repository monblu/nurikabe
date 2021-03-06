# Holds Nurikabe tables

""" "W" = white
    "B" = black
    "U" = undefined """

number_of_levels = 4 # Number of Tables

# Table 1
table1 = [["U", "U", "1", "U", "U", "2"],
         ["1", "U", "U", "U", "U", "U"],
         ["U", "U", "2", "U", "U", "2"],
         ["U", "2", "U", "U", "U", "U"]]

# Table 2
table2 = [["U", "2", "U", "U", "U"],
         ["U", "U", "U", "2", "U"],
         ["U", "U", "U", "U", "U"],
         ["U", "1", "U", "U", "U"],
         ["U", "U", "U", "U", "2"]]

# Table 3
table3 = [["U", "U", "U", "1", "U"],
         ["U", "U", "U", "U", "U"],
         ["U", "U", "3", "U", "4"],
         ["U", "1", "U", "U", "U"],
         ["U", "U", "U", "U", "U"]]

# Table 4
table4 = [["1", "U", "2", "U", "U", "2", "U"],
         ["U", "U", "U", "U", "U", "U", "U"],
         ["2", "U", "U", "4", "U", "U", "1"],
         ["U", "U", "U", "U", "U", "U", "U"],
         ["2", "U", "U", "U", "2", "U", "U"],
         ["U", "U", "4", "U", "U", "U", "U"],
         ["U", "U", "U", "U", "U", "U", "1"]]

# Table where we can draw :D
def create_table(x_len, y_len):
    """ Return a table full of "U" of dimensions x_len and y_len """
    tempTable = []
    for x in range(x_len):
        tempTable.append([])
        for y in range(y_len):
            tempTable[x].append("U")
    return tempTable


table_draw = [["U", "U", "U", "U", "U", "U", "U", "U", "U"],
              ["U", "U", "U", "U", "U", "U", "U", "U", "U"],
              ["U", "U", "U", "U", "U", "B", "U", "U", "U"],
              ["U", "U", "B", "U", "U", "U", "B", "U", "U"],
              ["U", "U", "U", "U", "B", "B", "B", "U", "U"],
              ["U", "U", "U", "U", "B", "U", "B", "U", "U"],
              ["U", "U", "B", "U", "U", "U", "B", "U", "U"],
              ["U", "U", "U", "U", "U", "B", "U", "U", "U"],
              ["U", "U", "U", "U", "U", "U", "U", "U", "U"],
              ["U", "U", "U", "U", "U", "U", "U", "U", "U"]]

# Table Generator (not in use)
tab_00 = """
u1uu
uuu2
1u2u
uuuu
uuuu
2u2u"""

tab_01 = tab_00.split() # split lines along white space

tab_02 = []
for line in tab_01:
    line = line.upper()
    character_list = list(line) # separates string in list of caracters
    print(line, character_list)
    tab_02.append(character_list)
    

#print('multiline string', tab_00)
#print('list of lines', tab_01)
#print('list of characters', tab_02)