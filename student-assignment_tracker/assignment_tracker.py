assignments = []
def PrintMenu():
    print("\n---Assignment Tracker----\n"
        "1. Add Assignment \n"
        "2. View Assignment \n"
        "3. Mark Complete \n"
        "4. Exit \n"
    )

def AddAssignment():
    assignment = []

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

def ViewAssignment():

    if not assignments:
        print("No assignments..")
    else:
        for index in range(len(assignments)):
            assignment = assignments[i]
            print(f"\nAssignment {index+1}")
            print("Subject:", assignment["Subject"])
            print("Title:", assignment["Title"])
            print("Due Date:", assignment["Due Date"])
            print("Priority:", assignment["Priority"])
            print("Status:", assignment["Status"])
            print("-------------------------")

def MarkComplete():
    print("Current assignments ---")

    if not assignments:
            print("No assignments..")
            return
    ViewAssignment()
    number = int(input("Enter assignment no: "))
    index = number - 1

    if 0<= index < len(assignments):
        assignments[index]["Status"] = "Completed"
        print("✅ Assignment marked as completed successfully!")
    else:
        print("❌ Invalid assignment number.")



while True:
    PrintMenu()
    option = int(input("Select an option : "))

    if option == 1:
        AddAssignment()

    elif option == 2:
        ViewAssignment()

    elif option == 3:
        MarkComplete()

    elif option == 4:
        print("Exiting Tracker ...\n")
        break
    else:
        print("Invalid Option ..")

#Try Switcher



