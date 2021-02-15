# This program will assist a small business in managing tasks assigned to each member of the team

import datetime #  importing datetime for saving current task added as current date. option 'a' on the menu.

login = False # The user is not logged in by default.
pw_confirm = False # used to confirm passwords of newly registered users. False as default
user_count = 0 #  counts total number of users
task_count = 0 #  counts total number of tasks

with open('tasks.txt' , 'r+') as f: #  opens tasks.txt to read in data. No need to close file in program as with open has always been used.
    user = [] #  empty lists ready for entries
    title = [] 
    task = []
    date_added = []
    date_due = []
    completed = []

    for line in f: #  filling lists with data from tasks.txt
        line = line.split(", ") #splitting lists by mentioned structure.

        user.append(line[0]) #  adding in all specified data
        title.append(line[1])
        task.append(line[2])
        date_added.append(line[3])
        date_due.append(line[4])
        completed.append(line[5])
        task_count += 1 #  counting total number of tasks registered.

        
with open("user.txt" , "r+") as g: # opens user.txt to read in date.
    username = [] #  empty lists ready for entries
    password = []

    for line in g: #  filling lists with data from tasks.txt
        line = line.strip()
        line = line.split(", ") #  splitting lists by mentioned structure.

        username.append(line[0]) #  adding in all specified data
        password.append(line[1])
        user_count += 1 #  counting total number of users registered.



while login != True: #  allowing a user to login. 
    user_username = input("Please enter your username ")
    user_password = input("Please enter your password ")
    
    for i in range(user_count): #  checking user login credentials
        if username[i] == user_username and password[i] == user_password:
            login = True
            print("Welcome {}\n".format(user_username))
    print("You have entered the wrong username / password")

if  user_username == "admin": #  displaying special menu for admin
    choice = input("Please select one of the following options : \nr - register user \na - add task"
               "\nva - view all tasks \nvm - view my tasks \ns - show statistics \ne - exit\n")
else:
    choice = input("Please select one of the following options : \nr - register user \na - add task" #  displaying normal user menu. This is repeated throughout.
                       "\nva - view all tasks \nvm - view my tasks \ne - exit\n")
    
    



while choice != 'e': #creating a menu to loop through. 'e' to exit.
    
    if choice == "r": #  registering a new user
        print("Register a new user")
        if user_username == 'admin': #  only an admin can add a new user
            while pw_confirm != True: # checking if new password matches password typed in the first time.
            
                username = input("Please enter the new user's username ")
                password = input("Please enter the new user's password ")
                password_check = input("Please enter your password again ")
            
                if password == password_check:
                
                    pw_confirm = True
                
                    with open("user.txt" , "a") as f: #  writing new user to user.txt
                        f.write("\n" + username + ", " + password)
                        print("\nUser {} has been added".format(username))
            
        else: #  letting users know about permissions.
            print("Sorry you do not have permission to enter a new user. You must be an admin")
            
        if  user_username == "admin":
            choice = input("Please select one of the following options : \nr - register user \na - add task"
                           "\nva - view all tasks \nvm - view my tasks \ns - show statistics \ne - exit\n")
        else:
            choice = input("Please select one of the following options : \nr - register user \na - add task"
                       "\nva - view all tasks \nvm - view my tasks \ne - exit\n")

    elif choice == "a": #  adding a new task
        print("add a task")
        user = input("Enter the username of the person the task is assigned to ") #  capturing data for new task
        title = input("Please enter in a title of the task ")
        task = input("Please enter in the details of the task ")
        date_due = input("Pleae enter in the due date - day month year ")
        date_added = datetime.datetime.now()
        date_added = date_added.strftime("%d %b %Y") #  date added must be current date. no need for input. pulls current date in specified format. Please refer to reference at the bottom.
        completed = "No"

        with open("tasks.txt" , "a") as f: #  writing new task to tasks.txt
            f.write("\n" + user + ", " + title + ", " + task + ", " + date_added + ", " + date_due + ", " + completed)
            
            if  user_username == "admin":
                choice = input("Please select one of the following options : \nr - register user \na - add task"
                           "\nva - view all tasks \nvm - view my tasks \ns - show statistics \ne - exit\n")
            else:
                choice = input("Please select one of the following options : \nr - register user \na - add task"
                       "\nva - view all tasks \nvm - view my tasks \ne - exit\n")
        
    elif choice == "va": #  viewing all tasks

        print("View all tasks")
        with open("tasks.txt" , "r") as f:
            for i in range(task_count): # writing all tasks saved in task.txt to lists.
                print("__________________________________________")
                print("Task :         \t{}".format(title[i]))
                print("Assigned to: \t{}".format(user[i]))
                print("Date assigned:\t{}".format(date_added[i]))
                print("Due Date:      \t{}".format(date_due[i]))
                print("Task Complete:\t{}".format(completed[i]))
                print("Task desc:\t{}".format(task[i]))

            if  user_username == "admin":
                choice = input("Please select one of the following options : \nr - register user \na - add task"
                           "\nva - view all tasks \nvm - view my tasks \ns - show statistics \ne - exit\n")
            else:
                choice = input("Please select one of the following options : \nr - register user \na - add task"
                       "\nva - view all tasks \nvm - view my tasks \ne - exit\n")


    elif choice == "vm": #  view tasks for logged in user.
        print("View my tasks")
        with open("tasks.txt" , "r") as f: # printing all tasks saved in tasks.txt
                for i in range(task_count):
                    if user[i] == user_username: #  tasks must be related to logged in user
                        print("__________________________________________")
                        print("Task :         \t{}".format(title[i]))
                        print("Assigned to: \t{}".format(user[i]))
                        print("Date assigned:\t{}".format(date_added[i]))
                        print("Due Date:      \t{}".format(date_due[i]))
                        print("Task Complete:\t{}".format(completed[i]))
                        print("Task desc:\t{}".format(task[i]))

                if  user_username == "admin":
                    choice = input("Please select one of the following options : \nr - register user \na - add task"
                           "\nva - view all tasks \nvm - view my tasks \ns - show statistics \ne - exit\n")
                else:
                    choice = input("Please select one of the following options : \nr - register user \na - add task"
                       "\nva - view all tasks \nvm - view my tasks \ne - exit\n")

    elif choice == "s" and user_username == "admin": #  stat menu for admin only.
        print("The total number of users is: {}".format(user_count)) # using counts defined in the beginning
        print("The total number of tasks is: {}".format(task_count))
        choice = input("\nPlease select one of the following options : \nr - register user \na - add task"
               "\nva - view all tasks \nvm - view my tasks \ns - show statistics \ne - exit\n")

    else:
        print("You have entered an invalid option. Please choose again")
        choice = input("\nPlease select one of the following options : \nr - register user \na - add task"
                       "\nva - view all tasks \nvm - view my tasks \ne - exit\n")



#Refernces : Datetime - https://www.w3schools.com/python/python_datetime.asp
