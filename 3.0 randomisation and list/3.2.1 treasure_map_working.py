# enter position and mark an x in that position

row1=['✅','✅', '✅'];
row2=['✅','✅', '✅'];
row3=['✅','✅', '✅'];


map=[row1, row2, row3];
# if user B1

# print(map)
# print(map[0][1])
# print(map)
# desired structure
print(f"{row1}\n{row2}\n{row3}")


# take position from user

position=input("Pleas enter the position you want to mark as visited for example 'B1' "); 
# EG B1, A1 ETC
letter=position[0].upper()
number=position[1]
print(f"letter: {letter} and number : {number}" )
# index():but how
ABC=["A","B", "C"];

index_letter=ABC.index(letter)
print("printing the index of letter")
print(index_letter)
# convert the number to index
index_number=int(number)-1;
print("My numbers........")
print(index_number)

# USING THE NOTION OF NESTED LISTS
map[index_letter][index_number]='❌'

print("CHOSEN POSITION.......")
print(f"{row1}\n{row2}\n{row3}")