expenses = []

def addExpense():
    print("Add")

def viewExpenses():
    print("Hello")

def menu():
    

    while True:
        print("1.Add Expense" 
            "\n2. View Expenses" 
            "\n3. Exit")
            
        choice = int(input("Choose an option: "))
        
        if choice == 1:
            addExpense()
        elif choice == 2:
            viewExpenses()
        elif choice == 3:
            print("Exiting.. ")
            break
        else:
            print("\nInvalid choice! Try again")

def main():

    print("\n------ Expense Tracker ------")
    
    menu()

main()