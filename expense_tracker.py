# Function to add an expense to the list of expenses
def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})

# Function to print all expenses in a formatted way
def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')

# Function to calculate and return the total expenses
def total_expenses(expenses):
    return sum(map(lambda expense: expense['amount'], expenses))

# Function to filter expenses based on a specified category
def filter_expenses_by_category(expenses, category):
    return filter(lambda expense: expense['category'] == category, expenses)

# Main function to interact with the user and manage the expense tracker
def main():
    # List to store the expenses
    expenses = []

    # Main loop for the expense tracker
    while True:
        # Display menu options
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')

        # Get user choice
        choice = input('Enter your choice: ')

        # Process user choice
        if choice == '1':
            amount = float(input('Enter amount: '))
            category = input('Enter category: ')
            add_expense(expenses, amount, category)

        elif choice == '2':
            print('\nAll Expenses:')
            print_expenses(expenses)

        elif choice == '3':
            print('\nTotal Expenses: ', total_expenses(expenses))

        elif choice == '4':
            category = input('Enter category to filter: ')
            print(f'\nExpenses for {category}:')
            expenses_from_category = filter_expenses_by_category(expenses, category)
            print_expenses(expenses_from_category)

        elif choice == '5':
            print('Exiting the program.')
            break

# Entry point of the program, only run main() if the script is executed directly
if __name__ == '__main__':
    main()
