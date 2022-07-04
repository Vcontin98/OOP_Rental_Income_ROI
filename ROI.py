class ROI:
    def __init__(self):
        self.income = 0
        self.expenses = 0
        self.investment = 0
        self.roi = 0       

    def get_income(self):
        income_inputs = {}
        print("\nUse only whole numbers with no commas or periods.\nIf none, type 0.\n")
        income_inputs['rental']= input("Rental income: ")
        income_inputs['laundry']= input("Laundry income: ")
        income_inputs['storage']= input("Storage income: ")
        income_inputs['misc']= input("Miscellaneous income: ")
        for key, value in income_inputs.items():
            if value == '':
                value = 0
            self.income += int(value)
        print(f"\nYour total monthly income is:\n\t${self.income}\n")

    def get_expenses(self):
        exp_inputs = {}
        print("\nUse only whole numbers with no commas or periods.\nIf none, type 0.\n")
        exp_inputs['mortgage']= input("Mortgage payment: ")
        exp_inputs['tax']= input("Property taxes: ")
        exp_inputs['insurance']= input("Insurance: ")
        exp_inputs['utilities']= input("Utilities: ")
        exp_inputs['hoa']= input("HOA fees: ")
        exp_inputs['lawn']= input("Lawn and/or snow services: ")
        exp_inputs['vacancy']= input("Vacancy costs: ")
        exp_inputs['repairs']= input("Repairs: ")
        exp_inputs['capital expenditures']= input("Capital expenditures: ")
        exp_inputs['property management']= input("Property Management: ")
        for key, value in exp_inputs.items():
            if value == '':
                value = 0
            self.expenses += int(value)
        print(f"\nYour total monthly expenses are:\n\t{self.expenses}\n")

    def get_investment(self):
        inv_inputs = {}
        print("\nUse only whole numbers with no commas or periods.\nIf none, type 0.\n")
        inv_inputs['dn_payment']= input("Down payment: ")
        inv_inputs['closing']= input("Closing costs: ")
        inv_inputs['rehab']= input("Remodel costs: ")
        inv_inputs['misc']= input("Miscellaneous costs: ")
        for key, value in inv_inputs.items():
            if value == '':
                value = 0
            self.investment += int(value)
        print(f"\nYour total invesment is:\n\t{self.investment}\n")

    def update_info(self):
        while True:
            print("Which information you would like to update?\n")
            update_ask = input("1. Income\n2. Expenses\n3. Investments\n")
            if update_ask == '1':
                self.income = 0
                self.get_income()
            elif update_ask == '2':
                self.expenses = 0
                self.get_expenses()
            elif update_ask == '3':
                self.investment = 0
                self.get_investment()
            else:
                update_ask = input("Please type a number: \
                1. Income \
                2. Expenses \
                3. Investments")
            ask = input("Would you like to update other information? (y/n) ")
            if ask == 'n':
                break
        self.roi = 0
        self._roi()
    
    def _roi(self):
        import time
        length = input('Enter the range in years for your ROI: ')
        print("\nWhew! Thanks for all that information! Let's calculate your Return on Investment...")
        length = int(length)
        length *= 12
        time.sleep(3)
        print('your income is: ' + str(self.income))
        print('your expenses is: '+ str(self.expenses))
        print('your investment is: '+ str(self.investment))
        print(f'your length is '+ str(length))
        annual_cash = (self.income - self.expenses) * length
        self.roi = round((annual_cash / self.investment) * 100, 2)
        print(f"\nYour projected Return on Investment is {self.roi}%\n")
        
def run_roi():
    import time
    print("Welcome to Bigger Pockets ROI Calculator!\nWe'll take you step-by-step to find your projected real estate profits\n")
    z = ROI()
    print("Let's start with your expected monthly INCOME.\n")
    z.get_income()
    time.sleep(1)
    print("Now we'll go through your monthly EXPENSES\n")
    z.get_expenses()
    time.sleep(1)
    print("Finally, let's look at INVESTMENTS.\n")
    z.get_investment()
    time.sleep(2)
    z._roi()
    while True:
        print("What do you think?")
        more = input("1. This is great! I'm ready to roll!\n2. I want to change some information...")
        while more not in {'1', '2'}:
            print("We'd love to stay and play all day, but we know you have money to make!")
            more = input("Please choose:\n1. I have all the information I need. (exits the calculator)\n2. I want to change some things to see if I can make more money! (keep working...)\n")
        if more == '1':
            print("\nThanks for using Bigger Pockets ROI Calculator! Best of luck to you!")
            break
        elif more == '2':
            z.update_info()
            
run_roi()