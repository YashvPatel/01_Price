def calculate_cost(file_size_bytes, cost_per_unit):
    # Convert file size from bytes to units
    file_size_units = file_size_bytes

    # Calculate cost in units
    cost_units = file_size_units * cost_per_unit

    return cost_units


# Example usage
file_size_bytes = 5000  # Size of file in bytes

# Prompt the user for their preference
unit_preference = input("Enter 'g' for grams or 'kg' for kilograms: ")

# Set the cost per unit based on user preference
if unit_preference == 'g':
    cost_per_unit = 0.001  # Cost per gram
elif unit_preference == 'kg':
    cost_per_unit = 1  # Cost per kilogram
else:
    print("Invalid input. Assuming grams as the unit.")
    cost_per_unit = 0.001  # Default cost per gram

# Calculate cost
cost_units = calculate_cost(file_size_bytes, cost_per_unit)

# Print the result
print("Cost in", unit_preference, ":", cost_units)
