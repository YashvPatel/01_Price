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
want_explanation = yes_no("Is this your first time: ")  # Swap "yes" and "no"

if want_explanation == "yes":  # Swap "yes" and "no"
    explanation = ["A thorough explanation of this program is to compare and contrast",
                   "different type of rices in cost & kgs to best match your preferred",
                   "type of rice",
                   ""]
    print("")
    for step in explanation:
        print(step)

print("You may continue")
print()