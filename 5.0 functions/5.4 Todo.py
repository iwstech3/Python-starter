# we need a list
# alias empty bucket
todo_list=[]
# first functionality
# add to the list
def add_todo():
    # what to add?
    item=input("Enter a todo✝✡: ")
    todo_list.append(item)
    print("item added successfully")
    
# DELETE FUNCTIONALITY
def delete_todo():
    if len(todo_list)==0:
        print("ooh, list is empty💔")
    else:
        for index, item in enumerate(todo_list):
            # print("TODO ITEMS 🥗\n");
            print(f"{index + 1}. {item}")
    number_to_remove=int(input("Enter the item number to remove 🍖"))-1
    if number_to_remove<0 or number_to_remove>=len(todo_list):
        print("out of range 🍳_________")
    else:
        del todo_list[number_to_remove];
        print("Item removed successfully...👓")
def update_todo():
    if len(todo_list)==0:
        print("ooh, list is empty💔")
    else:
        for index, item in enumerate(todo_list):
            # print("TODO ITEMS 🥗\n");
            print(f"{index + 1}. {item}")
    number_to_update=int(input("Enter the item number to update 🍖"))-1
    if number_to_update<0 or number_to_update>=len(todo_list):
        print("out of range 🍳_________")
    else:
        new_item=input("enter new item")
        todo_list[number_to_update]=new_item;
        
    
def view_list():
    if len(todo_list)==0:
        print("ooh, list is empty💔")
    else:
        # show the items inside of the list
        for index, item in enumerate(todo_list):
            print(f"{index+1}. {item}")
    
    
while True:
    print("MY TODO LIST APP: ")
    print("1.add to do ")
    print("2. Remove from todo")
    print("3. Update todo:")
    print("4. view todo")
    print("5. quit")
    choice=input("enter number to compute from above ")
    if choice=="1":
        add_todo()
    elif choice=="2":
        delete_todo()
    elif choice=="3":
        update_todo()
    elif choice=="4":
        view_list()
    elif choice=="5":
        break;
    else:
        print("stupid, try agin, you don't have sense?tsuuiipp")

    
        