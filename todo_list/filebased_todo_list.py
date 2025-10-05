#Learnt file handling with differet modes
#functions with params and return
#file handling with "with" keyword

TASK_FILE_PATH = "./todo_list/my_tasks.txt"
MENU = """
1. Add Task
2. Display Tasks
3. Delete task
4. Clear All
5. Exit
"""

def read_tasks():
    try:
        with open(TASK_FILE_PATH,'r') as tasks_file_handle:
            return tasks_file_handle.read().splitlines()
    except FileNotFoundError:
        print("Invalid file path")

def write_tasks(all_tasks_list: list):
    try:
        with open(TASK_FILE_PATH,'w') as tasks_file_handle:
            if (all_tasks_list):
                for task in all_tasks_list:
                    if (task.strip()):
                        tasks_file_handle.write(f"{task}\n")
    except FileNotFoundError:
        print("Invalid file path")
    except IOError as ex:
        print(f"Error writing to file \n {ex}")


def print_all_tasks(all_tasks: list):
    if (all_tasks):
        print("\nYour tasks:")
        for i, task in enumerate(all_tasks, 1):
            print(f"{i}. {task}")
    else:
        print("\nNo tasks to display\n")

print("Welcome to your Todo List")
my_task_list = list()

while True:
    try:
        user_action_choice = int(input(MENU + "Enter your choice: ").strip())
        if (user_action_choice == 1):
            new_task_title = input("\nEnter task title: ").strip()
            if (new_task_title):
                all_tasks = read_tasks()
                all_tasks.append(new_task_title)
                write_tasks(all_tasks)
            else:
                print("\nInvalid title\n")
        elif (user_action_choice == 2):
            print_all_tasks(read_tasks())
        elif (user_action_choice == 3):
            all_tasks = read_tasks()
            print(all_tasks)
            delete_task_title = input("\nEnter task to delete: ").strip()
            if (delete_task_title): 
                if (delete_task_title in all_tasks):
                    all_tasks.remove(delete_task_title)
                    write_tasks(all_tasks)
                else:
                    print("\nTask not present\n")
            else:
                print("\nInvalid task\n")
        elif (user_action_choice == 4):
            write_tasks(None)
        elif (user_action_choice == 5):
            print("\nBye!\n")
            break
    except IndexError:
        print("Index not present")
    except(ValueError):
        print("Incorrect option picked")