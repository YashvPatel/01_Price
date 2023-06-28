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


# main routine goes here
want_instructions = yes_no("Want me to display the Rice List, comparing prices in grams? ")

if want_instructions == "yes":
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

print("you may continue")
print()


# currency formatting function
def currency(x):
    return "${:.2f}".format(x)


# Gets expense, returns list which has
# the data frame and subtotal
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

    # loop to get component, quantity and price
    item_name = ""
    while item_name.lower() != "xxx":

        print()
        # get name, quantity and item
        item_name = not_blank("Item name: ",
                              "The item name can't be blank.")

        if item_name.lower() == "xxx":
            break

        if var_fixed == "variable":
            quantity = num_check("Kgs:", "The amount must be a whole number which is more than zero", int)

        else:
            quantity = 1

        price = num_check("How much for a single item? $", "The price must be a number <more than 0>", float)

        # add item, quantity and price to lists
        item_list.append(item_name)
        quantity_list.append(quantity)
        price_list.append(price)

        expense_frame = pandas.DataFrame(variable_dict)
        expense_frame = expense_frame.set_index('item')

        expense_frame['Cost'] = expense_frame['Quantity'] * expense_frame['Price']
        # Find sub-total
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
yes_no_list = ['yes', 'no']


# Ask user for profit goal
def profit_goal(total_costs):
    # Initialise variables and error message
    error = "Please enter a valid weight\n"

    while True:

        # ask for profit goal...
        response = input("what is valid weight (eg 5000g or 5kgs) ")

        # check if first character is $...
        if response[0] == "$":
            profit_type = "$"
            # Get amount (everything after the $)
            amount = response[1:]

        # check if last character is %
        elif response[-1] == "%":
            profit_type = "%"
            # Get amount (everything before the %)
            amount = response[:-1]

        else:
            # set response to amount for now
            profit_type = "unknown"
            amount = response

        try:
            # Check amount is a number more than zero...
            amount = float(amount)
            if amount <= 0:
                print(error)
                continue

        except ValueError:
            print(error)
            continue

        if profit_type == "unknown" and amount >= 100:
            dollar_type = yes_no("Do you mean {:.2f}g. "
                                 "ie {:.2f} Grams?, "
                                 "y / n ".format(amount, amount))

            # Set profit type based on user answer above
            if dollar_type == "yes":
                profit_type = "$"
            else:
                profit_type = "%"

        elif profit_type == "unknown" and amount < 100:
            percent_type = yes_no("Do you mean {}kgs? , "
                                  "y / n".format(amount))

            if percent_type == "yes":
                profit_type = "%"
            else:
                profit_type = "$"

        # return profit goal to main routine
        if profit_type == "$":
            return amount
        else:
            goal = (amount / 100) * total_costs
            return goal


profit_target = profit_goal(100)
print(profit_target)

# Get product name
product_name = not_blank("Product name: ", "The product name can")

print()
print("Please enter your weight below...")

variable_expenses = get_expenses("variable")
variable_frame = variable_expenses[0]
variable_sub = variable_expenses[1]

# Write data to file

# *** Printing Area ****

# Find Total Costs
print()
print("**** Price Comparison Tool - {} *****".format(product_name))
print()
expense_print("Rice Total", variable_frame, variable_sub)
