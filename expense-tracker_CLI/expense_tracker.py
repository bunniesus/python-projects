Expenses = []

def addExpense():

    date = input("Enter date: ")
    amount = float(input("Enter Amount: "))
    category = input("Enter category: ")
    description = input("Write description: ")

    expense = {
        "date" : date,
        "amount" : amount,
        "category" : category,
        "description" : description
    }
    Expenses.append(expense)
    print("Expense added Successfully!\n")
    

def viewExpenses():

    if not Expenses:
        print("No data added!")
    else:
        for i in range (len(Expenses)):
            expense = Expenses[i]
            print("----------- Expenses ------------")
            print(f"\n{i + 1} ."    )
            print("DATE : ", expense['date'])
            print("AMOUNT : ", expense['amount'])
            print("CATEGORY : ", expense['category'])
            print("DESCRIPTION : ", expense['description'])
            print("-------------------------")


def menu():
    

    print("\n------ Expense Tracker ------")

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
    
    menu()


main()