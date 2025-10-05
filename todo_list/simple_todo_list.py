#Writing a short app to learn basics of lists

#This is a terminal-based transient memory todo list without the bells & whistles 

#Learnt the following:
#input(), f-string, """, None, 
#append, pop(i), clear, type casting to int, chained comparison
#try, except, ValueError, IndexError blocks
#intro to functions

print("Welcome to your Todo List")

my_task_list = list()
menu = """
1. Add Task
2. Display Tasks
3. Delete task
4. Clear All
5. Exit
"""

def print_current_tasks():
    print("\nCurrent Tasks:")
    for i, task in enumerate(my_task_list, 1):
        print(f"{i}. {task}")

while True:
    #Display a menu to pick from 
    str_choice = input(f"{menu}\nSelect option: ")
    if (str_choice): 
        #if input is not empty
        try:
            #if input is a number
            int_choice = int(str_choice)
            #add task
            if (int_choice == 1):
                task_title = input("\nEnter Task Title: ")
                if (task_title):
                    my_task_list.append(task_title)
                    print_current_tasks()
            #print all tasks
            elif (int_choice == 2):
                if (len(my_task_list) == 0):
                    print("\nWoohoo! No tasks to worry about now")
                else:
                    print_current_tasks()
            #delete tasks
            elif (int_choice == 3):
                #Delete only when there are tasks available
                if (len(my_task_list) > 0):
                    task_to_delete = input("\nEnter Task Number to Delete: ")
                    #if the task_to_delete is not empty
                    if (task_to_delete):
                        #if task_to_delete is a number
                        try:
                            # Convert to int first, then compare
                            task_number = int(task_to_delete)
                            if (1 <= task_number <= len(my_task_list)):
                                my_task_list.pop(task_number - 1)
                                print_current_tasks()
                            else:
                                #when the index entered does not have a corresponding task
                                print("That task number does not exist \n")
                        except ValueError:
                            #when a non-number is entered to be deleted
                            print("Please enter a valid number\n")
                        except IndexError:
                            #when a negative number is entered
                            print("Exception. That task number does not exist\n")
                    else:
                        print("Enter a number to delete")
                    
                else:
                    print("No task to delete\n")
            #clear all tasks
            elif (int_choice == 4):
                confirm = input("Enter y to confirm & any key to cancel: ").lower()
                if (confirm == "y"):
                    my_task_list.clear()
                else:
                    print("Cancelled.")
                    print_current_tasks()
            #exit app
            elif (int_choice == 5):
                break
            #picked invalid menu option but an integer
            elif (int_choice not in (1,2,3,4,5)):
                print ("Invalid Choice (Pick one from menu)\n")
                continue
        #entered an option which is not a number
        except:
            print("\nInvalid Choice (Not a number)")
            continue
    #No option entered
    else:
        print("\nInvalid Choice (None selected)")
        continue

