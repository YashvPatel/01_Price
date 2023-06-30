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
