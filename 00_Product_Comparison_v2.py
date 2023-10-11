# import libraries
import pandas


# checks users enter a number that is more than zero.
# Can be used to check for integers or floats
def num_check(question, error, num_type):
    valid = False
    while not valid:
        try:
            response = num_type(input(question))
            if response <= 0:
                print(error)
            else:
                return response
        except ValueError:
            print(error)


# checks that user has entered yes / no to a question
def yes_no(question):
    to_check = ['yes', 'no']
    valid = False
    while not valid:
        response = input(question)
        for var_item in to_check:
            if response == var_item:
                return response
            elif response == var_item[0]:
                return var_item
        print("Please enter either yes or no...\n")


# checks that a response is not blank
def not_blank(question, error):
    valid = False
    while not valid:
        response = input(question)
        if response == "":
            print("{}. \nPlease try again.\n".format(error))
            continue
        return response


# currency formatting function
def currency(x):
    return "${:.2f}".format(x)


# instructions go here
want_explanation = yes_no("Do you need an explanation of this program?: ")

if want_explanation == "yes":
    explanation = ["Begin by typing in your budget", "", "Then type in the name of the item you want",
                   "to compare, the weight / volume of the item", "(in grams to kgs) and the price.", ""
                                                                                                      "",
                   "Program will calculate the unit price and recommend",
                   "the product which is the best value for money.", ""]
    print("")
    for step in explanation:
        print(step)


# Gets expenses, returns list which has the data frame and subtotal
def get_expenses(var_fixed):
    item_list = []
    quantity_list = []
    price_list = []

    variable_dict = {
        "Item": item_list,
        "Quantity": quantity_list,
        "Price": price_list
    }

    # loop to get component, quantity and price
    item_name = ""
    while item_name.lower() != "xxx":
        print()
        # get name, quantity, and item
        item_name = not_blank("Item name: ", "The component name can't be blank.")
        if item_name.lower() == "xxx":
            break

        if var_fixed == "variable":
            quantity = num_check("Grams:", "The amount must be a whole number more than zero", int)
        else:
            quantity = 1

        price = num_check("How much? $", "The price must be a number <more than 0>", float)

        # add item, quantity, and price and lists
        item_list.append(item_name)
        quantity_list.append(quantity)
        price_list.append(price)

    expense_frame = pandas.DataFrame(variable_dict)
    expense_frame = expense_frame.set_index('Item')

    print()
    # Calculate cost of each component
    expense_frame['Cost'] = expense_frame['Quantity'] * expense_frame['Price']

    # Calculate cost per kilogram (cost per kg)
    expense_frame['Cost per kg'] = expense_frame['Cost'] / (expense_frame['Quantity'] / 1000)

    # Currency Formatting (uses currency function)
    add_dollars = ['Price', 'Cost', 'Cost per kg']
    for item in add_dollars:
        expense_frame[item] = expense_frame[item].apply(currency)

    return [expense_frame, expense_frame['Cost'].sum()]


# Prints expenses, returns list which has
def expense_print(heading, frame, subtotal):
    print()
    print("**** {} Costs ****".format(heading))
    print(frame)
    print()
    print("{} Costs: ${:.2f}".format(heading, subtotal))
    return ""


# *** Main routine starts here ***

print("Please enter your variable costs below...")
# Get variable costs
variable_expenses = get_expenses("variable")
variable_frame = variable_expenses[0]
variable_sub = variable_expenses[1]

# Calculate total costs
all_cost = variable_sub

# Calculate recommended price
selling_price = all_cost

# Print the list of variable costs at the end
print("**** Price Comparison Tool ****")
print(variable_frame.to_string())

# Find the lowest cost item
lowest_cost_item = variable_frame[variable_frame['Cost'] == variable_frame['Cost'].min()]

# Print the lowest cost item
print("\nLowest Cost Item:")
print(lowest_cost_item.to_string(index=False))
