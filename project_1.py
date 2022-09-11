class returnOnInvestment():
    """
        Attributes: income will be a dictionary, expenses will be a dictionary
    """
    def __init__(self, income, expenses, cash_flow):
        self.income = []
        self.expenses = []
        self.cash_flow = []
        
    def showIncome(self):
        state_income = input("Which source of income would you like to state? Rental/Laundry/Storage/Misc: ")
        
        if state_income.lower() == 'rental':
            rental = int(input("Please state your rental income: "))
            self.income.append(rental)
            
        elif state_income.lower() == 'laundry':
            laundry = int(input("Please state your laundry income: "))
            self.income.append(laundry)
            
        elif state_income.lower() == 'storage':
            storage = int(input("Please state your storage income: "))
            self.income.append(storage)
            
        elif state_income.lower() == 'misc':
            storage = int(input("Please state your miscellaneous income: "))
            self.income.append(storage)
            
        elif state_income.lower == 'quit':
            pass
         
        else:
            print("Try another command")
        
        monthly_income = int(sum(self.income))
            
        print(f"Your total monthly income is: {monthly_income}")
            
    def showExpenses(self):
        state_expense = (input(" Which expense would you like to state? Tax/Insurance/Utilities/Repairs/Mortgage/Other: "))
              
        if state_expense.lower() == 'tax':
            tax = int(input("Please state your tax expense: "))
            self.expenses.append(tax)
              
        elif state_expense.lower() == 'insurance':
            insurance = int(input("Please state your insurance expense: "))
            self.expenses.append(insurance)
              
        elif state_expense.lower() == 'utilities':
            utilities = int(input("Please state your utilities expense: "))
            self.expenses.append(utilities)
              
        elif state_expense.lower() == 'repairs':
            repairs = int(input("Please state your repairs expense: "))
            self.expenses.append(repairs)
            
        elif state_expense.lower() == 'mortgage':
            mortgage = int(input("Please state your mortgage expense: "))
            self.expenses.append(mortgage)
            
        elif state_expense.lower() == 'other':
            other = int(input("Please state any other expenses: "))
            self.expenses.append(other)
            
        elif state_expense.lower == 'quit':
            pass
        
        else:
            print("Try another command")
       
        monthly_expenses = int(sum(self.expenses))
        
        print(f"Your monthly expenses total to: {monthly_expenses}")
              
    def showCashFlow(self):
        current_cashFlow = sum(self.income) - sum(self.expenses)
        self.cash_flow.append(current_cashFlow)
        print(f"Current cash flow is: {current_cashFlow}")
        
    
              
    def showROI(self):
        total_investment = int(input("Please state your total investment: "))
        cashFlow = sum(self.cash_flow)
        annual_cashFlow = cashFlow * 12
        ROI = (annual_cashFlow / total_investment) * 100
    
        print(f"Our cash on cash ROI = {ROI} percent.")

house_Value = returnOnInvestment([], [], [])

def run():
    while True:
        response = input("Select one of the following options. (select Income if just beginning): Income/Expenses/Cash Flow/ROI - Quit to end - ")
        
        if response.lower() == 'income':
            house_Value.showIncome()
        elif response.lower() == 'expenses':
            house_Value.showExpenses()
        elif response.lower() == 'cash flow':
            house_Value.showCashFlow()
        elif response.lower() == 'roi':
            house_Value.showROI()
        elif response.lower() == 'quit':
            break
        else:
            print("Try another command")
            
run()