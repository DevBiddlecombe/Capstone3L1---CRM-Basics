# This program will assist a small business in managing tasks assigned to each member of the team

import datetime
from datetime import datetime #  importing datetime for saving current task added as current date. option 'a' on the menu.


#  Defining empty / boolean variables before program

user_count = 0 #  counts total number of users
task_count = 0 #  counts total number of tasks
login = False # The user is not logged in by default.

#  Reading in both user.txt and tasks.txt

with open('tasks.txt' , 'r+') as f: #  opens tasks.txt to read in data. No need to close file in program as with open has always been used.
    user = [] #  empty lists ready for entries
    title = [] 
    task = []
    date_added = []
    date_due = []
    completed = []
    task_num = []

    for line in f: #  filling lists with data from tasks.txt
        line = line.split(", ") #splitting lists by mentioned structure.

        user.append(line[0]) #  adding in all specified data
        title.append(line[1])
        task.append(line[2])
        date_added.append(line[3])
        date_due.append(line[4])
        completed.append(line[5])
        task_num.append(line[6])
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

#  User defined functions to be used in the menu. Defined functions must be listed first.

# Registering a new user. To register a new user you must be logged in as an admin


def reg_user():
    print("Register a new user")
    pw_confirm = False # used to confirm passwords of newly registered users. False as default
    if user_username == 'admin': #  only an admin can add a new user
        while pw_confirm != True: # checking if new password matches password typed in the first time.
            
            new_username = input("Please enter the new user's username ") #  Asking for user login details
            password = input("Please enter the new user's password ")
            password_check = input("Please enter your password again ")
            duplicate = False
            
            if password == password_check:
                
                pw_confirm = True

        with open('user.txt' , 'r' ) as f: #  Checking if the register the user wants to register is already on the database
            for i in range(user_count):
                if new_username == username[i]:
                    duplicate = True
                    print("Sorry this user is already registered")
                
        if duplicate == False:
            with open("user.txt" , "a") as f: #  writing new user to user.txt
                f.write("\n" + new_username + ", " + password)
                print("\nUser {} has been added".format(new_username))

    else: #  letting users know about permissions.
            print("Sorry you do not have permission to enter a new user. You must be an admin")
    

def add_task(): # Method to add a task to tasks.txt
    print("add a task")
    user = input("Enter the username of the person the task is assigned to ") #  capturing data for new task
    title = input("Please enter in a title of the task ")
    task = input("Please enter in the details of the task ")
    date_due = input("Pleae enter in the due date - day month year ")
    date_added = datetime.datetime.now()
    date_added = date_added.strftime("%d %b %Y") #  date added must be current date. no need for input. pulls current date in specified format. Please refer to reference at the bottom.
    completed = "No"

    with open("tasks.txt" , "a") as f: #  writing new task to tasks.txt
        f.write("\n" + user + ", " + title + ", " + task + ", " + date_added + ", " + date_due + ", " + completed+", " + str(task_count+1))


def view_all(): #  Viewing all tasks saved on tasks.txt
    print("View all tasks")
    file = open("tasks.txt" , "r+")
    for line in file:
        task = line.split(",")
        print("*********************************************************************")
        print("Task manager: "+task[0]+"\nTask Subject: "+task[1]+"\nTask Details: "+task[2]+"\nDate Issued: "+task[3]+"\nDeadline: "+task[4]+"\nComplted: "+task[5]+"\nTask Number: " + task[6])
    file.close()
        
            
def view_mine(): # Viewing tasks to the user that is logged in. User can edit certain aspects of the task.
    print("View my tasks\n")
    user_task_count = 0
    file = open("tasks.txt" , "r+")
    for line in file:
        task = line.split(",")
        if task[0] == user_username: #  tasks must be related to logged in user
            print("Task Number: "+task[6]+"Task manager: "+task[0]+"\nTask Subject: "+task[1]+"\nTask Details: "+task[2]+"\nDate Issued: "+task[3]+"\nDeadline: "+task[4]+"\nComplted: "+task[5]+"\n")
            user_task_count += 1
    file.close()

    if user_task_count == 0: #  Allowing the user the option to edit existing tasks. Change complete, change user or due date with certain parameters.
        print("You have no tasks")

    if user_task_count != 0:
        amend = int(input("Select a task to change or -1 to exit\n"))

    if amend == -1: #  Exiting the sub menu
        print("Goodbye")


    if line != "": # If the user has tasks assigned they are able to edit certain parts.
        edit_choice = input("What would you like to do? \n1: Mark as complete \n2: Edit the deadline \n3: Edit the user assigned to task \n4: Edit the due date\n-1: Exit sub menu\n")

        if edit_choice == "1": #  Marking complete
            update_completed(amend, edit_choice)
            edit_choice = input("What would you like to do? \n1: Mark as complete \n2: Edit the deadline \n3: Edit the user assigned to task \n4: Edit the due date\n-1: Exit sub menu\n")

        if edit_choice == "2": #  Changing the deadline. 
            update_completed(amend, edit_choice)
            edit_choice = input("What would you like to do? \n1: Mark as complete \n2: Edit the deadline \n3: Edit the user assigned to task \n4: Edit the due date\n-1: Exit sub menu\n")

        if edit_choice == "3": #  Changing user assigned to task
            update_completed(amend, edit_choice)
            edit_choice = input("What would you like to do? \n1: Mark as complete \n2: Edit the deadline \n3: Edit the user assigned to task \n4: Edit the due date\n-1: Exit sub menu\n")

    line = update_completed(amend, edit_choice) # Running method update_completed with variables entered above.
            
            
def update_completed(amend, edit_choice): #  Updating the task assigned to the user from view_mine.

    file = open("tasks.txt" , "r") # Reading in tasks.txt
    list_of_lines = file.readlines() # Adding contents from tasks.txt to list_of_lines for manipulation.
    file.close()
    if edit_choice == "1":
        list_of_lines[amend-1] = (user[amend-1]+", "+title[amend-1]+", "+task[amend-1]+", "+date_due[amend-1]+", "+date_added[amend-1]+", "+"yes"+", "+task_num[amend-1]) # Updating completion 
        
    if edit_choice == "2":
        new_deadline = input("Please enter the new deadline for the job - DD MON YEAR (21 Jan 2021 as example)")
        list_of_lines[amend-1] = (user[amend-1]+", "+title[amend-1]+", "+task[amend-1]+", "+new_deadline+", "+date_added[amend-1]+", "+completed[amend-1]+", "+task_num[amend-1]) # updating new deadline
        
    if edit_choice == "3":
        if completed[amend-1] == "no": #  Can only change the task if it is not completed.
            new_user = input("Please enter the name of the new user")
            list_of_lines[amend-1] = (new_user+", "+title[amend-1]+", "+task[amend-1]+", "+date_due[amend-1]+", "+date_added[amend-1]+", "+completed[amend-1]+", "+task_num[amend-1]) # Updating user task is assigned to
        else:
            print("Sorry you cannot change this task as it is marked as complete") # Can only change tasks if they are not complete

    file = open("tasks.txt" , "w") #  Writing new lines to tasks.txt
    file.writelines(list_of_lines)
    file.close()

# Generating a task report based on requirements.
       
def generate_report_tasks(): 
    task_complete = 0 # Creating variables before running them.
    task_uncomplete = 0
    i = 0 # Counter to go through tasks.txt
    j = 0 # Variable for checking if overdue
    date_due_date = [] # Counter to go through tasks.txt - used a different counter for ease of reference.
    incomplete_overdue = 0 
    today = datetime.now() #  bringing in today's date to compare overdue tasks.
    
    f = open("tasks.txt" , "r") # Checking if task is completed
    for line in f:
        if completed[i] == "no":
            task_uncomplete += 1
            i += 1
        else:
            task_complete += 1
            i += 1
    f.close()
    
    
    f = open("tasks.txt" , "r") # Checking if task is over due
    for line in f:
        date_due_date = datetime.strptime(date_due[j], '%d %b %Y')
        if date_due_date < today and completed[j] == 'no':
            incomplete_overdue += 1
            j += 1
            
        else:
            j += 1
    f.close()
                    
    percent_uncomplete = (task_uncomplete / task_count * 100)
    percent_complete = (task_complete / task_count * 100)
    with open('task_overview.txt' , 'w') as f: # Writing task report to a new txt file - task_overview.txt
        f.write("Total Number of tasks: {}\nTotal Number of completed tasks: {}\nTotal Number of incompleted tasks: {}"
                "\nIncomplete and overdue {}\nPercentage of tasks incomplete {}\nPercentage of tasks overdue {}".format(task_count , task_complete , task_uncomplete , incomplete_overdue, percent_uncomplete, incomplete_overdue/task_count*100))

# Method for generating the user report
    
def generate_report_users(): 
    user_task_count = 0
    complete_count = 0
    still_complete = 0
    today = datetime.now() # Defining date to compare overdue tasks
    overdue_incomplete = 0

    f = open("user_overview.txt" , "w")
    f.write("Total users registered: {}\nTotal Tasks registered: {}\n".format(user_count, task_count))

    for x in range(user_count): # This nested loop will allow the user_overview to write a report for every user based on user counts and task counts. This means the database is not limited in capacity.
        for i in range(task_count): # x is used for each user and i is used for each part of the tasks.txt doc.
            if username[x] == user[i]:
                user_task_count +=1
            if username[x] == user[i] and completed[i] == "yes":
                complete_count +=1
            date_due_date = datetime.strptime(date_due[i], '%d %b %Y')
            if username[x] == user[i] and date_due_date < today and completed[i] == 'no':
                overdue_incomplete += 1

        perc_tasks_assigned = user_task_count/task_count*100 #Calculating figures for the report
        perc_assigned_completed = complete_count/user_task_count*100
        perc_incomplete = (user_task_count - complete_count)/user_task_count*100
        perc_incomplete_overdue = overdue_incomplete/user_task_count*100

        f = open("user_overview.txt" , "a") # Writing the report
        f.write("\nUser: {}\nTotal number of tasks assigned to {}: {}\n% of tasks assigned {}\n% of tasks assigned and completed {}\n% of tasks incomplete {}\n"
                "% of tasks incomplete and overdue {}\n".format(username[x],username[x],user_task_count,perc_tasks_assigned,perc_assigned_completed, perc_incomplete,perc_incomplete_overdue ))
    
        user_task_count = 0 # Setting variables back to 0 so when the nested loop is run for the next user, all variables are cleared.
        complete_count = 0
        overdue_incomplete = 0
        
                               
def menu():
    if  user_username == "admin": #  displaying special menu for admin
        print("\nPlease select one of the following options : \nr - register user \na - add task"
              "\nva - view all tasks \nvm - view my tasks \ns - show statistics \ngr - generate reports \ne - exit\n")
    else:
        print("Please select one of the following options : \nr - register user \na - add task" #  displaying normal user menu. This is repeated throughout.
              "\nva - view all tasks \nvm - view my tasks \ne - exit")

    
while login != True: #  allowing a user to login.
    
    user_username = input("Please enter your username ")
    user_password = input("Please enter your password ")
    
    for i in range(user_count): #  checking user login credentials
        if username[i] == user_username and password[i] == user_password:
            login = True
            print("Welcome {}\n".format(user_username))

menu()
choice = input("\nPlease enter an option ")
 

while choice != 'e': #creating a menu to loop through. 'e' to exit.
    
    if choice == "r": #  registering a new user
       reg_user()
       
       menu()
       choice = input("\nPlease enter an option ")

    elif choice == "a": #  adding a new task
        add_task()
            
        menu()
        choice = input("\nPlease enter an option ")
        
    elif choice == "va": #  viewing all tasks
        view_all()

        menu()
        choice = input("\nPlease enter an option ")


    elif choice == "vm": #  view tasks for logged in user.
        view_mine()

        menu()
        choice = input("\nPlease enter an option ")

    elif choice == "gr" and user_username == "admin":
        generate_report_tasks()
        generate_report_users()

        

        menu()
        choice = input("\nPlease enter an option ")

    elif choice == "s" and user_username == "admin": #  stat menu for admin only.
        print("The total number of users is: {}".format(user_count)) # using counts defined in the beginning
        print("The total number of tasks is: {}".format(task_count))
        choice = input("\nPlease select one of the following options : \nr - register user \na - add task"
               "\nva - view all tasks \nvm - view my tasks \ns - show statistics \ne - exit\n")

    else:
        print("You have entered an invalid option. Please choose again")

        menu()
        choice = input("\nPlease enter an option ")



#Refernces : Datetime - https://www.w3schools.com/python/python_datetime.asp
