# Cole McLain 
# Lab 02: Forward Chaining
# 10/23/25


from RuleLoader import Rule
from typing import Set, List

def forward_chain_logic(rules : list[Rule], initial_facts : List[str]) -> Set[str]:
    """
    Takes a set of facts to compare against Rules and returns a list of new facts
    """
    facts = set(initial_facts)
    new_fact_added = True

    # Loop through rules
    while new_fact_added:
        new_fact_added = False
        for rule in rules:
            conditions_needed = rule.if_rule
            new_fact = rule.then_rule
            condition1_met : bool = False # Numerical check
            condition2_met : bool = False # Cur warning level check
            
            # Check first fact against server status rule
            if conditions_needed.__contains__(initial_facts[0]):
                condition1_met = True
            
            if condition1_met and type(initial_facts[1]) == int:
                condition2_met = rule.check_numerical_conditions(initial_facts[1])

            # If both conditions met, add fact and break from loop
            if condition1_met and condition2_met and new_fact not in facts:    
                new_fact_added = True
                facts.add(new_fact)
                break
    derived_facts = list(facts - set(initial_facts))
    return derived_facts


def extract_goals(rules : list[Rule], final_facts : list[str]):
    """
    Takes a list of rules and final facts to extract diagnoses. Returns to
    get_diagnosis()
    """
    diagnoses = []
    recommendations = []
    for rule in rules:
        if final_facts == rule.if_rule:
            diagnoses.append(final_facts)
            recommendations.append(rule.then_rule)
    return {"diagnoses": diagnoses, "recommendations": recommendations}