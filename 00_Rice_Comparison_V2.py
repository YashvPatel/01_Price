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
    global weight_kg
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

        while True:
            try:
                weight = float(input("Enter the weight in grams: "))
                if weight < 1000:
                    print("Weight cannot be below 1000 grams. Please enter a valid weight.")
                    continue

                # Automatically convert weight to kilograms
                weight_kg = weight * 0.001
                print(f"Weight: {round(weight_kg, 1)} Kgs")
                break

            except ValueError:
                print("Please enter a valid weight.")

        if var_fixed == "variable":
            # Use the weight in kilograms for calculation
            quantity = weight_kg  # Use the converted weight in kilograms as the quantity
        else:
            quantity = 0.1

            # Check if adding the item exceeds the budget
        price = num_check("How much for a single item? $", "The price must be a number > 0", float)

        # Calculate the cost based on weight in kilograms
        item_cost = quantity * price  # This line calculates the cost using weight in kilograms
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
print("**** Price Comparison Tool - {} *****".format(product_name))
expense_print("Product Total", variable_frame, variable_sub)

# Check if budget is over the cost
if variable_sub > budget:
    print()
    print("Your cost is over the budget.")
else:
    print()
    print("Your cost is within the cost budget.")

# Print cheapest rice and recommend information
print(
    "\nThe cheapest Product is '{}' with a cost of {} per kg.".format(cheapest_rice_name, cheapest_rice_cost_per_kg))
