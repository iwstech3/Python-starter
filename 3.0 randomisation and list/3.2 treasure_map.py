# enter position and mark an x in that position

# ✅❎❌
row1=['✅','✅', '✅'];
row2=['✅','✅', '✅'];
row3=['✅','✅', '✅'];


map=[row1, row2, row3];
# if user B1

print(map)
print(map[0][1])


# take position from user

position=input("Pleas enter the position you want to mark as visited for example 'B1' ");

# get the individual items / i.e the number and the letter from the enter position. which is a string

letter=position[0].upper();
number=position[1]


print(letter, number)
# here we are getting the individual items:
# letter=B 
# number=2
ABC=['A', 'B', 'C'];

index_letter=ABC.index(letter);
# print(index_letter);

# get the index of the number

index_number=int(number)-1

# print(index_number)

# PRINTING THE SQUARES
# now that we are getting an index, use it and mark x i that position

map[index_number][index_letter]='❌'
# check_index=map.index(map[index_number][index_letter])

# print(check_index)


print(f"{row1}\n{row2}\n{row3}")
