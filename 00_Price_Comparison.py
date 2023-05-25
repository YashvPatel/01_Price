# import libraries
import pandas
import math

# Functions start here

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


# Checks that the user has entered yes / no to a question
def yes_no(question, to_check=None):

    to_check - ["yes", "no"]

    valid = False
    while not valid:

        response = input(question).lower()

        for var_item in to_check:
            if response == var_item:
                return response
            elif response == var_item[0]:
                return var_item

        print("Please enter either yes or no...\n")


# Loops to make testing faster...
for item in range(0, 6):
    want_help = yes_no("Do want to read the instructions? ")
    print("You said '{}'\n".format(want_help))


# Ensures that the string isn't blank
def not_blank(question, error):
    valid = False
    while not valid:
        response = input(question)

        if response == "":
            print("{}. \n Please try again. \n".format(error))
            continue

        return response