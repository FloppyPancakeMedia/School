# Cole McLain 
# Lab 02: Forward Chaining
# 10/23/25

import csv
from io import StringIO
from typing import Dict, Set, List, Any

IF_KEY = "if"
AND_KEY = "and"
THEN_KEY = "then"
RESULT_TYPE_KEY = "result_type"
# Constants for result_type values
RESULT_TYPE_PRIORITY = "PRIORITY"
RESULT_TYPE_RECOMMENDATION = "RECOMMENDATION"

class Rule:
    """
    Object for storing Rule information such as:
    - if rule
    - then rule
    - result type

    Also provides function for checking </> statements in rules
    """
    def __init__(self, if_rule, then_rule, result_type):
        self.if_rule : list[str] = if_rule
        self.then_rule = then_rule
        self.result_type = result_type
    
    def check_numerical_conditions(self, condition : int):
        """
        Converts rule (which is string) to >/< check against condition
        """
        condition_met : bool = False
 
        print(f"Now testing: condition = {condition} under rule {self.if_rule[1]}")
        
        if self.if_rule[1] == "<=4":
            if condition <= 4:
                condition_met = True
        elif self.if_rule[1] == ">4":
            if condition > 4:
                condition_met = True
        elif self.if_rule[1] == ">10":
            if condition > 10:
                condition_met = True
        elif self.if_rule[1] == "<=10":
            if condition <= 10:
                condition_met = True
        elif self.if_rule[1] == ">0":
            # This should only trigger if condition is critical and there's no necessity to check against a value
            condition_met = True

        return condition_met
        

    
    def __str__(self):
        return f"if: {self.if_rule}, then: {self.then_rule}, result: {self.result_type}"


def load_rules(path: str) -> List[Dict[str, Any]]:
    """
    Extracts CSV data and converts it into Rule objects
    """
    with open(path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rules = []
        for row in reader:
            # Build the 'if' value set
            if_set = list()
            if row.get(IF_KEY):
                if_set.append(row[IF_KEY])
            if row.get(AND_KEY):
                if_set.append(row[AND_KEY])
            row[IF_KEY] = if_set
            
            # Remove the 'and' key
            if AND_KEY in row:
                del row[AND_KEY]
            
            then = row[THEN_KEY]
            result_type = row[RESULT_TYPE_KEY]
            new_rule = Rule(if_set, then, result_type)
            rules.append(new_rule)
    return rules