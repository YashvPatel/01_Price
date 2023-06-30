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


# *** Main routine starts here ***

# Ask user for budget
budget = num_check("Enter your budget: $", "The budget must be a number > 0", float)

# Rest of the code...
