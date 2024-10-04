def task():
    tasks = [] #empty list
    print("--- Welcome To The Task Managaement App ---")
    total_task_number = int(input("Enter how many task you want to add = "))
    for i in range(total_task_number):
        task_name = input(f"Enter task {i} = ")
        tasks.append(task_name)
    print(f"Today's task are :\n{tasks}")

    while True:
        operation = int(input("Enter \n1-Add\n2-Update\n3-Delete\n4-View\n5-Exit/Stop"))
        if operation == 1:
            new_task = input("Enter task you want to add = ")
            tasks.append(new_task)
            print(f"Task {new_task} has been successfully added")        
        elif operation == 2:
            old_task = input("Enter task name you want to update = ")
            if old_task in tasks:
                updated_task = input("Enter new task = ")
                ind = tasks.index(old_task)
                tasks[ind] = updated_task
                print(f"Updated task {updated_task}")
        elif operation == 3:
            del_val = input("Which task you want to delete = ")
            if del_val in tasks:
                ind = tasks.index(del_val)
                del tasks[ind]
                print(f"Task {del_val} has been deleted")
        elif operation == 4:
            print(f"Total tasks = {tasks}")
        elif operation == 5:
            print("--- Closing the program ---")
        else:
            print("Invalid input")

task()

