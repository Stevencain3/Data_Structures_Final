
''' Create Task Function
    - Creates a task that the user can set up,
        -Title, description, priority, and due date
    -Will eventually write into a text file for saving data 
'''
def create_task():
    title = input("Would you enter the title of the task you would like to create: ")
    description = input("Please enter a short description of the task: ")
    priority = input("would you please enter if this is a high medium or low priority task:")

    print (title)

def main():
    create_task()








if __name__ == "__main__":
    main()