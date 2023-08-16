import pandas


# checks that a response is not blank
def not_blank(question, error):
    valid = False
    while not valid:
        response = input(question)

        if response == "":
            print("{}. \nPlease try again.\n".format(error))
            continue

        return response


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


# Main routine goes here
# yes / no checker, (simple)
def yes_no(question):
    while True:
        response = input(question)

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter either yes or no...\n")


# Currency formatting function
def currency(x):
    return "${:.2f}".format(x)


# Instructions go here
def display_instructions():
    instructions = ["+*+*+ Rice Price Comparison +*+*+", "", "{-=-= Rice Costs in Kgs & Grams =-=-=-}",
                    "  _________     _____   ___   _____   ______",
                    "_|Rice type|_  |Grams| |kgs| |Price| |Per kg|", "Arborio Rice]  |1000g| |1.0| |$1.00| |$1.00|",
                    "White Rice]    |3500g| |3.5| |$4.50| |$1.28|",
                    "Brown Rice]    |5000g| |5.0| |$3.50| |$7.00| ", "Bomba Rice]    |3000g| |3.0| |$2.00| |$1.50|",
                    "Jasmine Rice]  |5500g| |5.5| |$4.00| |$0.72|", " ________________________________________",
                    "[Recommendation: Jasmine Rice, $0.72 / kg]", "(ie: $1.44 for 2kg)"]

    print("List:")
    for step in instructions:
        print(step)


# instructions go here
want_explanation = yes_no("Do you need instructions?: ")

if want_explanation == "yes":
    explanation = ["A thorough explanation of this program is to compare and contrast",
                   "different type of rices in cost & kgs to best match your preferred",
                   "type of rice",
                   ""]
    print("")
    for step in explanation:
        print(step)

print("you may continue")
print()

# Display instructions
want_instructions = yes_no("Want me to display the Rice List, comparing prices in grams? ")

if want_instructions:
    display_instructions()

print("You may continue.\n")


# Gets expense, returns list which has the data frame and subtotal
def get_expenses(var_fixed):
    # Set up dictionaries and lists
    item_list = []
    quantity_list = []
    price_list = []

    variable_dict = {
        "item": item_list,
        "Quantity": quantity_list,
        "Price": price_list
    }

    # Loop to get component, quantity, and price
    while True:
        item_name = input("Item name (enter 'xxx' to print list): ")

        if item_name.lower() == "xxx":
            break

        if var_fixed == "variable":
            quantity = num_check("Kgs: ", "The amount must be a whole number which is more than zero", float)
        else:
            quantity = 0.1

        price = num_check("How much for a single item? $", "The price must be a number <more than 0>", float)

        # Add item, quantity, and price to lists
        item_list.append(item_name)
        quantity_list.append(quantity)
        price_list.append(price)

    expense_frame = pandas.DataFrame(variable_dict)
    expense_frame = expense_frame.set_index('item')

    expense_frame['Cost'] = expense_frame['Quantity'] * expense_frame['Price']
    expense_sub = expense_frame['Cost'].sum()

    add_dollars = ['Price', 'Cost']
    for item in add_dollars:
        expense_frame[item] = expense_frame[item].apply(currency)

    return [expense_frame, expense_sub]


# Prints expense frames
def expense_print(heading, frame, subtotal):
    print()
    print("**** {} Costs ****".format(heading))
    print(frame)
    print()
    print("{} Costs: ${:.2f}".format(heading, subtotal))
    return ""


# *** Main routine starts here ***

print()
print("Please enter your weight below...")

# Ask user for weight
while True:
    try:
        # Ask user for weight
        weight = float(input("Enter your weight in (Grams): "))
        unit = input("Type (G) to begin converting: ")

        if unit == "G":
            weight = weight * 0.001
            unit = "Kgs."
            print(f"Your weight is: {round(weight, 1)} {unit}")
            break
        else:
            print(f"{unit} was not valid")

    except ValueError:
        print("Please enter a valid weight.")

# Ask user for budget
budget = num_check("Enter your budget: $", "The budget must be a number > 0", float)

# Get product name
product_name = not_blank("Product name: ", "The product name can't be blank")

variable_expenses = get_expenses("variable")
variable_frame = variable_expenses[0]
variable_sub = variable_expenses[1]

# Calculate whether budget is over the cost
is_over_budget = variable_sub > budget

# Write data to file

# *** Printing Area ****

# Find Total Costs
print()
print("**** Rice Comparison Tool - {} *****".format(product_name))
print()
expense_print("Rice Total", variable_frame, variable_sub)

# Check if budget is over the cost
if is_over_budget:
    print("\nYour budget is over the cost.")
else:
    print("\nYour budget is within the cost.")
