Expenses = []

def add_expenses():
    """Add an expense"""
    try:
        amount = float(input('Enter amount spent: '))
        category = input('Enter category (food, bills, ...): ').lower()
        Note = input('Enter a note or description: ')
        Expense = {
            'amount': amount,
            'category': category,
            'Note': Note
        }
        Expenses.append(Expense)
        print('\nYou have successfully added an expense\n')
    except ValueError:
        print('Please input valid details!')

def view_expenses():
    """Display expenses"""
    if not Expenses:
        print('\nExpense list is empty\n')
        return

    print('----- Your expense list ------')
    for i, e in enumerate(Expenses, start=1):
        print(f'{i}.  ${e["amount"]}  |  {e["category"]}  | {e.get("Note", "")}')
    print('---------------------------------------\n')

def delete_expenses():
    if not Expenses:
        print('\nNo expense to delete\n')
        return

    view_expenses()

    try:
        num = int(input('Enter number to delete: '))
        if 1 <= num <= len(Expenses):
            removed = Expenses.pop(num - 1)
            print(f"\nDeleted: {removed['category']} - {removed.get('Note','')} (${removed['amount']}) successfully\n")
        else:
            print('\nInvalid number\n')
    except ValueError:
        print('\nPlease input a valid number\n')

def total_spent():
    total = sum(e['amount'] for e in Expenses)
    print(f'\nYour total spent is {total}\n')

def menu():
    """main menu loop"""
    while True:
        print("""
==========1: Add Expense ===========
==========2: View Expense ==========
==========3: Delete Expense ========
==========4: View Total ============
==========5: Exit ==================
""")
        try:
            choice = int(input('Enter a choice: '))
        except ValueError:
            print('Please input a valid number')
            continue

        if choice == 1:
            add_expenses()
        elif choice == 2:
            view_expenses()
        elif choice == 3:
            delete_expenses()
        elif choice == 4:
            total_spent()
        elif choice == 5:
            print('Your session has ended')
            break
        else:
            print('Please input a valid number')

if __name__ == '__main__':
    menu()
