# Jason Lewis
# CS210 AI Programming (F25 Bird)
# Lab 01 - Group A
# Shipping Cost Calculator
# Instructions:
#       This program calculates the shipping cost based on the package's Weight (in kg)
# and the Destination Zone (A, B, or C).
# https://lcc-cit.github.io/CS210-CourseMaterials/Labs/Lab01-Python/GroupA/CS210_Lab01_Instructions_GroupA.html

def calculate_shipping_cost(weight_kg, zone):
    """Calculates the total shipping cost based on weight (in KG) and zone (A/B/C)"""

    # Print details for output readability:
    print("\n--- Shipping Cost Check ---")

    # Convert zone to uppercase for error handling
    z = zone.upper()

    # Error Handling for weight_kg not being a number:
    try:
        weight = float(weight_kg)
    except (TypeError, ValueError):
        print("\nError: Weight must be a number (kg).\n")
        return None

    if z == "A":
        if weight <= 5:
            shipping_cost = 10.00
        elif weight < 10: #implicity > 5 here
            shipping_cost = 15.00
        else: #implicity > 10 here
            shipping_cost = 20.00

    elif z == "B":
        if weight <= 5:
            shipping_cost = 15.00
        elif weight < 10: #implicity > 5 here
            shipping_cost = 20.00
        else: #implicity > 10 here
            shipping_cost = 25.00

    elif z == "C":
        if weight <= 5:
            shipping_cost = 20.00
        elif weight < 10: #implicity > 5 here
            shipping_cost = 25.00
        else: #implicity > 10 here
            shipping_cost = 30.00

    else:
        print("\nError: Wrong zone type. Please enter either zone A / B / C\n")
        return None

    # Display the given weight (kg), the zone and the total cost of shipping:
    print(f"\nYour package weights {weight_kg:.2f} KG and is located in zone {z} so your total shipping cost is: ${shipping_cost:.2f}\n")
    return shipping_cost

# Example 1: Zone A with 30 KG >> Should be 20.00
calculate_shipping_cost(30, "A")
print("-" * 30)

# Example 2: Zone B with 5 KG >> Should be 15.00
calculate_shipping_cost(5, "B")
print("-" * 30)

# Example 3: Zone C with 7.1231 KG >> Should be 25.00
calculate_shipping_cost(7.1231, "c")
print("-" * 30)

# Example 4: Invalid shipping weight (abcd)
calculate_shipping_cost("abcd", "c")
print("-" * 30)

# Example 5: Invalid shipping zone 12345
calculate_shipping_cost("7", "12345")
print("-" * 30)
