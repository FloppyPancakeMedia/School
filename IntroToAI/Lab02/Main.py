# Cole McLain 
# Lab 02: Forward Chaining
# 10/23/25

from RuleLoader import Rule, load_rules
from ForwardChainEngine import extract_goals, forward_chain_logic
from pathlib import Path

cwd = Path.cwd()
CSV_PATH = str(cwd) + '/rules.csv'

def get_diagnosis(initial_facts) -> str:
    """
    Makes calls to forward chain engine, then extract goals
    to return a diagnosis
    """
    rules = load_rules(CSV_PATH)
    facts = forward_chain_logic(rules, initial_facts)
    print(facts)
    return extract_goals(rules, facts)


expected_input = ["optimal", "warning", "critical"]

use_user_input : bool = False
if use_user_input:
    # Main loop
    while True:
        print("Let me diagnose your server's condition. Type 'quit' at any time to exit")

        # Ask for current server status
        print("Please enter the warning level. Expecting 'optimal', 'warning', or 'critical': ")
        warning_level = input()
        warning_level = warning_level.lower()

        if warning_level == "quit": break

        # Check for valid server status input
        valid_input = False
        for i in expected_input:
            if i == warning_level:
                valid_input = True
        
        if not valid_input:
            print("Invalid input. Expected optimal, warning, or critical \n\n")
            continue
        

        # Ask for time since last checked
        print("Please enter how many hours since your last check: ")
        time_since = input()
        time_since = time_since.lower()
        if time_since == "quit": break

        # Check to make sure valid int was given as input
        try:
            time_since = int(time_since)
            if time_since < 0:
                print("Invalid input. Expected integer greater than 0 \n\n")
        except:
            print("Invalid input. Expected an integer as input \n\n")
            continue


        # Pass input to functions to generate recommendation
        print("Checking....")
        initial_facts : list = [warning_level, time_since]
        result = get_diagnosis(initial_facts)
        print(f"Priority level is {result["diagnoses"]} and you should {result["recommendations"]} \n\n")

else:
    initial_facts1 = ["optimal", 2]
    initial_facts2 = ["optimal", 11]
    initial_facts3 = ["warning", 2]
    initial_facts4 = ["warning", 8]
    initial_facts5 = ["critical", 4]

    result1 = get_diagnosis(initial_facts1)
    result2 = get_diagnosis(initial_facts2)
    result3 = get_diagnosis(initial_facts3)
    result4 = get_diagnosis(initial_facts4)
    result5 = get_diagnosis(initial_facts5)

    print(result1)
    print(result2)
    print(result3)
    print(result4)
    print(result5)