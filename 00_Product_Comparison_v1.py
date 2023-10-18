import pandas


# checks user response is not blank
def not_blank(question):
    while True:
        response = input(question)
        if response != "":
            return response
        else:
            print("This can't be blank, please enter a response")
            print()


# checks users enter an integer
def num_check(question):
    while True:
        try:
            response = float(input(question))
            return response
        except ValueError:
            print("Please enter an integer.")


# Calculate the cost per kilogram based on weight and cost
def calc_cost_per_kg(var_weight, var_cost):
    cost_per_kgs = (var_cost / var_weight) * 1000
    return round(cost_per_kgs, 2)


def yes_no(question):
    valid = False

    while not valid:

        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please answer yes/ no ")


# currency formatting function
def currency(x):
    return "${:.2f}".format(x)


# main routine starts here

def get_budget():
    while True:
        budget_input = input("Enter your budget: ")
        try:
            budget = float(budget_input)
            if budget < 2.00:
                print("Invalid budget. Please enter an amount that's above $2.")
            else:
                return budget
        except ValueError:
            print("Invalid input")


# main routine starts here

yes_no_list = ["yes", "no"]
item_list = []
weight_list = []
cost_list = []
cost_per_kg_list = []

variable_dict = {
    "item",
    "weight",
    "cost",
}

print("*- Price Comparison Tool -*")
print()

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

budget_value = get_budget()
print("Your budget is: ${:.2f}".format(budget_value))
print()

# loop to enter items (Main Routine)
while True:
    item_name = not_blank("Enter the item name or 'xxx' to quit: ")

    if item_name == 'xxx' and len(item_list) > 0:
        break
    elif item_name == 'xxx':
        print("You must enter at least one item before exiting")
        continue

    item_cost = num_check("Cost: $")
    if item_cost > budget_value:
        print("The cost is over the budget of ${:.2f}.".format(budget_value))
        print()
        continue

    weight = num_check("Weight (in grams): ")

    # check user entered weight is a positive number
    if weight > 0:
        pass
    else:
        print("Weight must be above 0")
        continue

    print("Item: {}".format(item_name))
    print("Weight: {} grams".format(weight))
    print("Cost: ${:.2f}".format(item_cost))

    # Calculate the cost per kilogram for this item and append to the list
    cost_per_kg = calc_cost_per_kg(weight, item_cost)
    cost_per_kg_list.append(cost_per_kg)

    item_list.append(item_name)
    weight_list.append(weight)
    cost_list.append(item_cost)

print()
print("Selected items: ", item_list)

# Printing Code, Create a pandas DataFrame
data = {
    "Item Name": item_list,
    "Grams": weight_list,
    "Cost": cost_list,
    "Per kg": cost_per_kg_list
}
DataFrame = pandas.DataFrame(data)

# Print the DataFrame with price per kilogram
print()
print("{*=-.- Product Cost Per (kg) -.-=*}")
print()
print(DataFrame)

# Finds the cheapest item per kilogram
cheapest_item = DataFrame.loc[DataFrame["Per kg"].idxmin()]
print("\n-*=+= Cheapest item  =+=*-")
print("\n(Cheapest Item Per kg)")
print(cheapest_item)
