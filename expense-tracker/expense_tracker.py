import json 

Expenses = []

def addExpense():

    
    print("╭────────── ADD EXPENSE ──────────╮\n")
    date = input("Date (DD-MM-YYYY): ")
    amount = float(input("Amount (₹): "))
    category = input("Category: ")
    description = input("Description: ")

    expense = {
        "date" : date,
        "amount" : amount,
        "category" : category,
        "description" : description
    }

    Expenses.append(expense)

    print("✅ Expense added Successfully!\n")
    print("╰─────────────────────────────────╯")
    saveExpenses()


def loadExpenses():
    with open("expense-tracker/expenses.json", "r") as file_pointer:
        loaded_expenses = json.load(file_pointer)
    return loaded_expenses

def saveExpenses():
    with open("expense-tracker/expenses.json", "w") as file_pointer:
        json.dump(Expenses, file_pointer, indent = 2)

def viewExpenses():

    if not Expenses:
        print("No data added!")
    else:
        for i in range (len(Expenses)):  # can be -- for i, expense in enumerate(Expenses):
            
            expense = Expenses[i]
            print("\n╭──────────── YOUR EXPENSES ────────────╮")

            print(f"\n #{i + 1} "    )
            print(f"  📅 Date        : {expense['date']}")
            print(f"  💰 Amount      : ₹{expense['amount']:.2f}")
            print(f"  🏷️ Category     : {expense['category']}")
            print(f"  📝 Description : {expense['description']}")

            print("\n╰───────────────────────────────────────╯")

def monthlySummary() :
    total = 0
    category_totals = {}

    #PROCESS DATA
    for expense in Expenses:
        total += expense["amount"]

        if expense["category"] in category_totals:
            category_totals[expense["category"]] += expense["amount"]
        else: 
            category_totals[expense["category"]] =  expense["amount"] 

    #PRINT RESULTS
    print("\n╭──────────── MONTHLY SUMMARY ────────────╮")
    print(f"  💰 Total Spent      : ₹{total: .2f}")
    print("\n  🏷️ Category Breakdown     ")

    for category in category_totals:
        print(f"  {category: <15} : ₹{category_totals[category]: .2f}")

    print("\n╰───────────────────────────────────────╯")


def menu():

    print("\n╭───────────────────────────────────────╮")
    print("|             EXPENSE TRACKER           |")
    print("╰───────────────────────────────────────╯")

    while True:
        print("1. Add Expense" 
            "\n2. View Expenses" 
            "\n3. Monthly Summary"
            "\n4. Exit")
            
        choice = int(input("\nChoose an option: "))
        
        if choice == 1:
            addExpense()
        elif choice == 2:
            viewExpenses()
        elif choice == 3:
            monthlySummary()
            print("\n ")
        elif choice == 4:
            print("Exiting.. ")
            break
        else:
            print("\nInvalid choice! Try again")

def main():

    global Expenses
    Expenses = loadExpenses()
    menu()


main()
