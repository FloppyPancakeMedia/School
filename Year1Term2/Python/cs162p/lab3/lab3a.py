## Takes a method-type and inNum as arguments and calculates the result of the inNum ##
import sys

def result1(result : int, inNum : int):
    # Iterative approach. Takes variable to store result and int we want to calculate result of
    while (inNum > 1):
        result *= inNum
        inNum -= 1
    return result

def result2(inNum : int, result : int):
    # Recursive approach. Takes var to store result and int we want result of
    result *= inNum
    if inNum == 1: 
        return result
    
    return result2(inNum - 1, result)
    

methodType : str = sys.argv[1]
inNum : int = int(sys.argv[2])

# Main program #
if methodType == "iterative":
    result : int = 1
    print(result1(result, inNum))

elif (methodType == "recursive"):
    result : int = 1
    print(result2(inNum, result))

else:
    print("Please enter either 'iterative' or 'recursive' as the first arg")


