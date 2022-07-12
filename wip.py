from pydoc import importfile
#choose between raws, customers, margins

#globals


productlist = []

class Product:
    def __init__(self, item, vendor, price, state, freight):
        self.item = item
        self.vendor = vendor
        self.price = price
        self.state = state
        self.freight = freight
        self.cost = self.compute_cost()

    def compute_cost(self):
        if self.freight > 0.00:
            self.cost = self.freight + self.price
        else:
            self.cost = self.price
        
        return self.cost
    
    def print_string(self):
      return f'|Item: {self.item:s}|Vendor: {self.vendor:s}|Price: {self.price:f}|State: {self.state:s}|Freight: {self.freight:f}|Cost: {self.cost:f}|'

    def save_string(self):
      return f'{self.item:s},{self.vendor:s},{self.price:f},{self.state:s},{self.freight:f},{self.cost:f}'

    def display_string(self):
      return f'|{self.item:^10s}|{self.vendor:^10s}|{self.price:^10f}|{self.state:^10s}|{self.freight:^10f}|{self.cost:^10f}|'

def process_inputs(inputlist, separator=None):
    global productlist

    # raw_input = inputlist.split(separator)

    raw_input = inputlist #this might be repetitive

    item = raw_input[0]
    vendor = raw_input[1]
    price = float(raw_input[2])
    state = raw_input[3]
    freight = float(raw_input[4])
    
    cost = float(raw_input[5])

    products = Product(item,vendor,price,state,freight,cost)
    productlist.append(products)

    return products


def submit_new_product():
    global productlist

    item = input("Enter the Item: >>")
    vendor = input("Enter the Vendor: >>")
    price = float(input("Enter the Cost per pound: >>"))
    state = input("Enter the State: >>")
    freight = float(input("Enter the Freight: >>"))
    
    inputlist = item, vendor, price, state, freight

    new_product = process_inputs(inputlist)

    print(new_product.print_string())

def edit_product():
    pass
    
def raws_choice():
    raws_input = int(input("Enter 1 to add new product, 2 to edit a product: >>"))
    if raws_input == 1:
        submit_new_product()
    elif raws_input == 2:
        edit_product()
    else:
        print("invalid choice")

#main

quit = False
while not quit:
    menu_choice = int(input("Enter 1 for raws, 2 for customers, 3 for margins, 4 to quit: >>"))

    if menu_choice == 1:
        raws_choice()
    elif menu_choice == 2:
        customer_choice()
    elif menu_choice == 3:
        margins_choice()
    elif menu_choice == 4:
        quit = True
    else: 
        print("invalid choice")



