# INSTRUCTIONS
# 1. TAKE 2 PEOPLE for example luis and Grace: 
name1=input("Enter name 1: ");
name2=input("Enter name2: ");

# 2.  combine the two names
combine_names=name1 + name2;

# 3. check the number of times the letters in the word true (TRUE) occurs  in the combine names
t=combine_names.count("t");
r=combine_names.count("r");
u=combine_names.count("u");
e=combine_names.count("e")

add_true=t+r+u+e;
print(add_true)


# LOVE


l=combine_names.count("l");
o=combine_names.count("o");
v=combine_names.count("v");
e=combine_names.count("e")

add_love=l+o+v+e;

final_score = str(add_true) + str(add_love)
print(f"{add_true}{add_love}")
print(final_score)


# 4. check the number of times the  the letters in the word LOVE occurs in the combine names

# 5. Combine or concatenate 3 and 4 to make a digit and thats your love score

# CONDITIONS TO CHECK TO PRINT OUTPUT
# --IF love_Score > 90 Romeo and Ju
# --if love_Score > 70  but less than  89-> wawa
# --if love_SCore >60 but less than 79 -> Message