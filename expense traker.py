
def expense_tracker():
    expenses = []
    
    print("Welcome to Expense Tracker!")
    print("Enter 'done' when finished.")
    
    while True:
        category = input("\nEnter expense category (food, transport, etc.): ")
        if category.lower() == 'done':
            break
            
        try:
            amount = float(input("Enter amount spent: "))
            expenses.append({'category': category, 'amount': amount})
        except ValueError:
            print("Please enter a valid number for amount.")
    
    if expenses:
        print("\n--- Your Expenses ---")
        total = 0
        for expense in expenses:
            print(f"{expense['category']}: ${expense['amount']:.2f}")
            total += expense['amount']
        print(f"\nTotal expenses: ${total:.2f}")
    else:
        print("No expenses were recorded.")

if __name__ == "__main__":
    expense_tracker()
