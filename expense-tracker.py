"""
	-> We are defining an expense tracker program 

	-> The add_expense function:
		-> There are three arguments to this function 
		-> Expenses <- A list 
		-> Amount <- The amount which the expense was for 
		-> Category <- The category that the person spent the money in 
and category; this is a dictionary 
		-> Take this expense, and add a dictionary representation of it to the `expenses` list

	-> The print_expenses(expenses) function:
		-> This function takes the `expenses` list / dictionary as its argument 
		-> Take this list of expenses and iterate through them 
		-> Return the amount and category of each expense 

	-> The total_expenses(expenses) function:
		-> This calculates the total expenses 
		-> We take the expense amount from the different elements with a lambda function 
		-> Then we sum all of them up and return the figure 
		-> The aim is to define the function is as few lines as possible, to make it as concise as possible 

	-> filter_expenses_by_category(expenses, category):
		-> We are filtering the expenses based on their category 
		-> When we call this function, we are telling it to return a list of different expenses which match 
            the category which is input as an argument to the function 
		-> This is done using filtering 
		-> return filter(lambda expense: expense['category'] == category, expenses)
		-> filter <- Return the results for which this condition is true 
		-> lambda <- Search for the elements / entries in the main list of expenses, and return the ones which 
            match the category which we have asked for in the function argument   

	-> The main() function:
		-> This function is the entrypoint of the program 
		-> We are initialising an empty list of expenses and asking the user to enter expenses multiple times 
            <- a while loop 
		-> The options we are giving the user are 
			-> Adding an expense
			-> Listing all expenses 
			-> Showing the total expenses 
			-> Filtering expenses by category <- This is done with the function previously defined 
			-> Exiting the program 
		-> The user can add an expense <- In which case the amount and category of the expense will be asked for 
		-> They can also list all expenses <- In which case we print out all of the expenses in the terminal, or 
            where the function is being run 
			-> This is with the print_expenses() function   
		-> The third option does a similar thing to the second one, except that we are returning the total sum of 
            all of the expenses
		-> The fourth option to this:
			-> Filtering expenses by category 
			-> Calling the filter_expenses_by_category() function in this case <- filtering and printing expenses 
                from the category 
		-> The final option is that the user chooses to exit the program, in which case we execute a break and the 
            program terminates 
	-> This gives us a command line interface for tracking expenses 
"""

def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})

def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')
    
def total_expenses(expenses):
    return sum(map(lambda expense: expense['amount'], expenses))
    
def filter_expenses_by_category(expenses, category):
    return filter(lambda expense: expense['category'] == category, expenses)
    
def main():
    expenses = []
    while True:
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')
        
        choice = input('Enter your choice: ')

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

if __name__ == '__main__':
    main()