
class ExpenseTracker:

    def __init__(self):
        self.expense=[]

    def add_expense(self):
        
        name=input("Enter expense name: ")
        amount=float(input("Enter amount: "))

        expense={
            "name": name,
            "amount": amount
        }

        self.expense.append(expense)

        print("Expense added successfully")

    def show_expense(self):

        if not self.expense:
            print("No expenses found.")
            return
        
        print("\n---Expense List---")

        for e in self.expense:
            print(f"{e['name']} : {e['amount']}")
    
    def total_expense(self):

        total=0

        for e in self.expense:
            total+=e["amount"]

        print(f"\nTotal Expenses: {total}")

tracker=ExpenseTracker()

running=True

while running:

    print("\n---Expense Tracker---")
    print("1. Add Expense")
    print("2. Show Expenses")
    print("3. Show Total Expense")
    print("4. Exit")

    choice=input("Enter your choice: ")

    if choice=="1":
        tracker.add_expense()
    
    elif choice=="2":
        tracker.show_expense()
    
    elif choice=="3":
        tracker.total_expense()

    elif choice=="4":
        print("Existing program...")
        running=False
     
    else:
        print("Invalid choice!")



