

print("---Assignment Tracker----\n"
    "1. Add Assignment \n"
    "2. View Assignment \n"
    "3. Mark Complete \n"
    "4. Exit \n"
)

def AddAssignment():
    
    assignments = []

    subject = input("Enter Subject: ")
    title = input("Title: ")
    due = input("Due Date: ")
    priority = input("Priority: ")

    assignment = {
    "Subject" : subject, 
    "Title" : title, 
    "Due Date" : due,
    "Priority" : priority,
    "Status" : "Pending"
}
    assignments.append(assignment)
    
option = int(input("Select an option : "))

if option == 1:
    AddAssignment()

elif option == 2:
    print("View Assignment")
elif option == 3:
    print("Mark Copleted")
elif option == 4:
    print("Exiting Tracker ...")
else:
    print("Invalid Option ..")

#Try Switcher



