tasks = []

print("Super Simple To-Do List")
print("Commands: add, view, remove, quit")

while True:
    command = input("\n> ").lower()
    
    if command == "add":
        task = input("Task to add: ")
        tasks.append(task)
        print(f"Added '{task}'")
    
    elif command == "view":
        if not tasks:
            print("No tasks yet!")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
    
    elif command == "remove":
        if not tasks:
            print("No tasks to remove!")
        else:
            print("\nCurrent Tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            
            num = int(input("Task number to remove: "))
            removed = tasks.pop(num-1)
            print(f"Removed '{removed}'")
    
    elif command == "quit":
        print("\nFinal Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        print("Goodbye!")
        break
    
    else:
        print("Please type: add, view, remove, or quit")