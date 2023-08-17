import pandas


# checks that a response is not blank
def not_blank(question):
    while True:
        response = input(question)
        if response != "":
            return response
        else:
            print("This cant be blank")
            print()


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


# currency formatting function
def currency(x):
    return "${:.2f}".format(x)


# instructions go here
want_instructions = yes_no("Do you need the Rice Price Comparison list?: ")

if want_instructions == "yes":
    instructions = ["+*+*+ Rice Price Comparison +*+*+", "", "{-=-= Rice Costs in Kgs & Grams =-=-=-}",
                    "  _________     _____   ___   _____   ______",
                    "_|Rice type|_  |Grams| |kgs| |Price| |Per kg|", "Arborio Rice]  |1000g| |1.0| |$1.00| |$1.00|",
                    "White Rice]    |3500g| |3.5| |$4.50| |$1.28|",
                    "Brown Rice]    |5000g| |5.0| |$3.50| |$7.00| ", "Bomba Rice]    |3000g| |3.0| |$2.00| |$0.67|",
                    "Jasmine Rice]  |5500g| |5.5| |$4.00| |$0.73|", " ________________________________________",
                    "[Recommendation: Bomba Rice, $0.67 / kg]", "(ie: $1.34 for 2kg)", ""]
    print("List:")
    for step in instructions:
        print(step)

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

# Ask user for budget
budget = num_check("Enter your budget: $", "The budget must be a number > 0", float)


# Gets expense, returns list which has the data frame and subtotal
def get_cost(var_fixed, budget):
    # Set up dictionaries and lists
    item_list = []
    quantity_list = []
    price_list = []
    subtotal = 0

    variable_dict = {
        "item": item_list,
        "Quantity": quantity_list,
        "Price": price_list
    }

    # Loop to get component, quantity, and price
    while True:
        item_name = not_blank("Item name (enter 'xxx' to print list): ")
        if item_name.lower() == "xxx":
            break

        # Ask user for weight in grams
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

        if var_fixed == "variable":
            quantity = num_check("Kgs: ", "The amount must be a whole number which is more than zero", float)
        else:
            quantity = 0.1

        # Check if adding the item exceeds the budget
        price = num_check("How much for a single item? $", "The price must be a number > 0", float)

        item_cost = quantity * price
        if (subtotal + item_cost) <= budget:
            # Add item, quantity, and price to lists
            item_list.append(item_name)
            quantity_list.append(quantity)
            price_list.append(price)
            subtotal += item_cost
        else:
            print("This item exceeds the budget.")

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

# Get product name
product_name = not_blank("Product name: ")

variable_expenses = get_cost("variable", budget)
variable_frame = variable_expenses[0]
variable_sub = variable_expenses[1]

# Calculate whether budget is over the cost
is_over_budget = variable_sub > budget

# Determine the cheapest rice type and its cost per kilogram
cheapest_rice_row = variable_frame[variable_frame['Price'] == variable_frame['Price'].min()]
cheapest_rice_name = cheapest_rice_row.index[0]
cheapest_rice_cost_per_kg = cheapest_rice_row['Price'].values[0]

# *** Printing Area ****

# Find Total Costs
print()
print("**** Rice Comparison Tool - {} *****".format(product_name))
expense_print("Rice Total", variable_frame, variable_sub)

# Check if budget is over the cost
if variable_sub > budget:
    print()
    print("Your cost is over the budget.")
else:
    print()
    print("Your cost is within the cost budget.")

# Print cheapest rice and recommend information
print(
    "\nThe cheapest rice is '{}' with a cost of {} per kg.".format(cheapest_rice_name, cheapest_rice_cost_per_kg))
