# add item to list
# delete item from list
# update item from list
# read or view items from list
todo_list=[]
def add_list():
    
    item=input("Enter item to list ")
    todo_list.append(item)
    print(todo_list)
    print("item added successfully")
    
def delete_task():
    # check if task array is empty
    if len(todo_list)==0:
        print("No item in the list")
    else:
        # print items in the list
        for index, item in enumerate(todo_list):
            print("Item List......")
            print(f"{index + 1}. {item}")
        # enter task index you want to remove
        task_number=int(input("Enter the task number you want to remove"))-1
        if task_number<0 or task_number>=len(todo_list):
            print("Invalid task number")
        else:
            del todo_list[task_number]
            print("Item deleted successfully")
        
        
        
def update_task():
    # check if task array is empty
    if len(todo_list)==0:
        print("No item in the list")
    else:
        # print items in the list
        for index, item in enumerate(todo_list):
            print("Item List......")
            print(f"{index + 1}. {item}")
        # enter task index you want to remove
        task_number=int(input("Enter the task number you want to update"))-1
        new_item=input("Enter the new item to update")
        if task_number<0 or task_number>=len(todo_list):
            print("Invalid task number")
        else:
            todo_list[task_number]=new_item;
        
        
def view_task():
    if len(todo_list)==0:
        print("The todo list is empty")
    else:
        print("Current task")
        for index, item in enumerate(todo_list):
            print(f"{index+1}. {item}")    
# Main loop
while True:
    print("\n ________TODO_APP______")
    print("1. Add task")
    print("2. Delete Task")
    print("3. Update task")
    print("4. View Task")
    print("5. Exit app")
    choice=input("choose choice from above to add]")
    if choice=="1":
        add_list()
    elif choice=="2":
        delete_task()
    elif choice=="3":
        update_task()
    elif choice=="4":
        view_task()
    else:
        print("You picked an invalid choice from the list")
    
        
    

