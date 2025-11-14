# Jason Lewis
# CS210 AI Programming (F25 Bird)
# Lab 01 - Group A
# Financial Product Recommendation System
# Instructions:
#       Create a simplified expert system that recommends a suitable investment product based on two factors provided by the user.
# Investment Horizon (Short-Term: <5 years, or Long-Term: ≥5 years) and Risk Tolerance (Low or High).
# https://lcc-cit.github.io/CS210-CourseMaterials/Labs/Lab01-Python/GroupA/CS210_Lab01_Instructions_GroupA.html


def calculate_product(investment_horizon, risk_tolerance):
    """Calculates the financial product to recommend based on the users investment horizon and risk tolerance."""

    # Print details for output readability:
    print("--- Financial Product Recommendation ---")

    # Error Handling for investment_horizon not being a number:
    try:
        horizon = float(investment_horizon)
    except (TypeError, ValueError):
        print("Error: Investment Horizon must be a valid number of years.\n")
        return None
    # Error Handling for investment_horizon being a negative number:
    if horizon < 0:
        print("Error: Investment Horizon cannot be a negative number of years.\n")
        return None
    
   # Error Handling for risk_tolerance input being a string
    if not isinstance(risk_tolerance, str):
        print("Error: Risk Tolerance must be either 'low' or 'high'.\n")
        return None
    
    # String operations preformed after validating that it is a string.
    risk = risk_tolerance.strip().lower()

    # Input Validation risk input values: 'low' or 'high'
    if risk not in {"low", "high"}:
        print("Error: Risk Tolerance must be either 'low' or 'high'.\n")
        return None

    # Investment Horizon (Short-Term: <5 years, or Long-Term: ≥5 years)
    if horizon < 5 and risk == "low":
        product = "High-Yield Savings Account"
    elif horizon < 5 and risk == "high":
        product = "Short-Term Corporate Bonds"
    elif horizon >= 5 and risk == "low":
        product = "Government Bonds/Index Fund"
    elif horizon >= 5 and risk == "high":
        product = "Diversified Stock Portfolio"
    else:
        return None
    
    # Display the given factors and then the recommended financial product
    print(f"Your Investment Horizon: {horizon} Years\n")
    print(f"Your Risk Tolerance: {risk}\n")
    print(f"Your Recommended Financial Product: {product}")
    print("-" * 30 + "\n")

# Example 1: long term 7 years with low risk. Expected: Government Bonds/Index Fund
calculate_product(7, "low")
# Example 2: long term 80 years with high risk. Expected: Diversified Stock Portfolio
calculate_product(80, "high")
# Example 3: short term 3.5 years with low risk. Expected: High-Yield Savings Account
calculate_product(3.5, "Low")
# Example 4: short term 5 years with high risk. Expected: Short-Term Corporate Bonds
calculate_product(4, "high")
# Example 5: horizon bad input. Expected: Investment Horizon must be a valid number of years
calculate_product("abcd", "low")
# Example 6: horizon bad input. Expected: Error: Investment Horizon cannot be a negative number of years.
calculate_product(-5, "low")
# Example 7: horizon good input. Expected: Error: Investment Horizon cannot be a negative number of years.
calculate_product(5, "LLLOWWWW")