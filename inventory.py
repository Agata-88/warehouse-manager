from tabulate import tabulate
#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost = int, quantity = int):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
        '''
        In this function, you must initialise the following attributes:
            ● country,
            ● code,
            ● product,
            ● cost, and
            ● quantity.
        '''
    def get_cost(self):
        return self.cost
        '''
        Add the code to return the cost of the shoe in this method.
        '''

    def get_quantity(self):
        return self.quantity
        '''
        Add the code to return the quantity of the shoes.
        '''
    def __str__(self):
        return f"{self.country},{self.code},{self.product},{self.cost},{self.quantity}" 
        '''
        Add a code to returns a string representation of a class.
        '''
    def get_list(self):
        return f"{self.country},{self.code},{self.product},{self.cost},{self.quantity}"

#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
new_shoes_list = []
quantity_list = []
shoe_list = []
#==========Functions outside the class==============
''' 
read_shoes_data function opens inventory.txt file and reads data from the file.
for loop iterates through the lines of the file. Shoe object is created and appended
to the shoe_list.
'''
def read_shoes_data():
        try:
            with open("inventory.txt", "r") as f:
                split_shoes = f.readlines()
            for shoe_data in split_shoes[1:]:
                shoe_data = shoe_data.strip("\n").split(",")
                shoes = Shoe(shoe_data[0], shoe_data[1],shoe_data[2],shoe_data[3], shoe_data[4])
                shoe_list.append(shoes)
        except FileNotFoundError:
            print("Oops it looks like this file doesn't exist. Please double check and try again!")

'''
capture_shoes function allows user to create new shoe object by answering series of questions.
Object shoe is then appended to the shoe_list.
'''
def capture_shoes():
    read_shoes_data()
    country = input("Please enter country: \n")
    code = input("Please enter code: \n")
    product = input("Please enter product name: \n")
    cost = int(input("Please enter product cost: \n"))
    quantity = int(input("Please enter product quantity: \n"))
# Values are assigned to she object from user input
    shoe = Shoe(country,"SKU"f"{code}",product,cost,quantity)
    shoe_list.append(shoe)
    with open("inventory.txt", "w") as f:
        for lines in shoe_list:
            f.write(f"{lines}\n")

''' 
view_all function reads all shoe objects from the shoe_list. List comprehension
is used and result is displayed in tabulated format.
'''
def view_all():
    if len(shoe_list)==0:
        read_shoes_data()
    shoes = [shoe.get_list().split(",") for shoe in shoe_list]
    print(tabulate(shoes, headers=["Country", "Code", "Product", "Cost", "Quantity"]))

'''
re_stock funcion calls read_shoes_data function and then iterates through shoe list starting from index 1.
get_quantity method is called quantity values are appended to quantity list. Once the list is created minimum
value of the list is found. User is then asked if they would like to add more items to the lowest quantity item.
For loop is userd to iterate through the shoe_list and if shoe.quantity equals minimum quantity value, new_quantity
is added to it based number entered by user. Updated list gets printed.
'''
def re_stock():
    if len(shoe_list)==0:
        read_shoes_data()
    for shoes in shoe_list[1:]:
        count = shoes.get_quantity()
        count = int(count)
        quantity_list.append(count)
    min_quantity = min(quantity_list)
    print(min_quantity)
    min_quantity_index = quantity_list.index(min(quantity_list))
    print(f"Lowest quantity found is: {min_quantity} for shoe: {shoe_list[min_quantity_index+1]}")
    user_input = input("Would you like to re-stock this item? Press Y for Yes\n")
    if user_input == "Y" or user_input == "y":
        new_quantity = input("Enter number of items you would like to add to current stock: \n")
    for shoe in shoe_list:
        if shoe.quantity == str(min_quantity):
            shoe.quantity = int(min_quantity) + int(new_quantity)
            # for lines in shoe_list:
            #     print(lines)    
    with open("inventory.txt", "w") as f:
        f.write("Country,Code,Product,Cost,Quantity\n")
        for lines in shoe_list:
            f.write(f"{lines}\n")
'''
search_shoe function allows user to search for shoe object using
shoe code. User inputs code they are looking for and program
looks for that code and prints relevant shoe object.
'''
def search_shoe():
    code_search = input("Please enter code for the shoe you are looking for: \n")
    code_search = ("SKU"+str(code_search))
    if len(shoe_list)==0:
        read_shoes_data()
    for shoes in shoe_list: 
        if shoes.code == code_search:
            print(f"Shoe you are looking for is: {shoes}")
            
'''
value_per_item function calls read_shoes_data function and then iterates through
shoe_list. list_with_value variable gets created and it concatenate shoes and value.
for loop iterates through list_with_value and appends lines to new_shoes_list.
new_shoes_list is printed in tabulated format.
'''
def value_per_item():
    if len(shoe_list)==0:
        read_shoes_data()
    for shoes in shoe_list: 
        shoes.cost = int(shoes.cost)
        shoes.quantity = int(shoes.quantity)
        value = shoes.cost * shoes.quantity
        list_with_value = (f"{shoes}, {value}")
        for lines in [list_with_value]:
            lines = lines.strip("\n").split(",")
            new_shoes_list.append(lines)
    print(tabulate(new_shoes_list, headers = ["Country", "Code", "Product", "Cost", "Quantity", "Value"]))

'''
highest_qty funcions finds shoe object with highest quantity 
and prints it.
'''
def highest_qty():
    if len(shoe_list)==0:
        read_shoes_data()
    for shoes in shoe_list[1:]:
        count = shoes.get_quantity()
        count = int(count)
        quantity_list.append(count)
    max_quantity = max(quantity_list)
    max_quantity_index = quantity_list.index(max(quantity_list))
    print(f"This shoe is now for sale: {shoe_list[max_quantity_index+1]}")

#==========Main Menu=============

print("\u0332".join("Welcome to Nike warehouse stocktaking program!"))
user_choice = ""
while user_choice !="quit":
    user_choice = input("\nWhat would you like to do?:\nread data,\ncapture shoes,\nview all,\nre-stock,\nsearch shoe,\ndisplay value,\nhighest quantity:\n").lower()
    if user_choice == "read data":
        read_shoes_data()
    elif user_choice == "capture shoes":
        capture_shoes()
    elif user_choice == "view all":
        view_all()
    elif user_choice == "re-stock":
        re_stock()
    elif user_choice == "search shoe":
        search_shoe()
    elif user_choice == "display value":
        value_per_item()
    elif user_choice == "highest quantity":
        highest_qty()
    elif user_choice == "quit":
        print("Goodbye!")
    else:
        print("Sorry we don't recognise this input")