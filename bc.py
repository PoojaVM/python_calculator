import sys

# Holds all outputs to print
outputs = []
# Holds latest values of variables
state = {}


# Evaluates any expression given
def evaluate(exp):
    exp = exp.replace(" ", "")
    # Makes sure there are no brackets in the given expression
    if "(" not in exp and ")" not in exp:
        # Evaluating operators incase expression has no brackets
        return evaluate_operators(exp)

    curr_string = ""
    # Extracting contents of innermost bracket pair
    for e in exp:
        if e == "(":
            curr_string = ""
            continue
        if e == ")":
            # Evaluating the contents of the innermost bracket pair
            curr_result = evaluate(curr_string)
            # Replacing result of evaluation in place of the innermost bracket
            exp = exp.replace("(" + curr_string + ")", str(curr_result))
            return evaluate(exp)
        curr_string += e

    # Evaluating operators of the final expression
    # XXX - I don't think I need this anymore
    return evaluate_operators(exp)


# evaluate_operators decides order of execution of operations based on precedence
def evaluate_operators(string):
    nums = []
    ops = []
    num_str = ""
    var_str = ""
    for s in string:
        # Checking if char encountered is a variable
        # FIXME - vars can be multiple char words
        # TODO - Should probably throw an error if the variable isn't present in the dict
        if s.isalpha():
            var_str += s
            continue
        # else:
        #     nums.append(state[var_str])
        # Checking if char encountered is a number
        if s.isdigit() or s == ".":
            num_str += s
        else:
            # Adding number to nums list
            if num_str != "":
                nums.append(float(num_str))
                num_str = ""
            # Checking is char encountered is a valid operator
            if s in "^/%*-+":
                # Checking precedence of operators, starting from highest priority
                while ops and precedence(s) <= precedence(ops[-1]):
                    # Actually performing the operations
                    apply_operation(nums, ops)
                # Adding all operations to ops list
                ops.append(s)
    if var_str in state:
        nums.append(state[var_str])
    elif var_str not in state and var_str != "":
        nums.append(state[var_str])
    if num_str != "":
        nums.append(float(num_str))
    while ops:
        apply_operation(nums, ops)
    # After all operations performed, return the only element left in the list
    return nums[0]


# this function helps decide which operation is performed first
def precedence(op):
    if op in "^":
        return 3
    elif op in "/%*":
        return 2
    # elif op in "*":
    #     return 2
    elif op in "+-":
        return 1
    else:
        return 0


# Performs calculation
def apply_operation(nums, ops):
    b = nums.pop()
    a = nums.pop()
    op = ops.pop()
    if op == "^":
        nums.append(a**b)
    elif op == "/":
        nums.append(a / b)
    elif op == "%":
        nums.append(a % b)
    elif op == "*":
        nums.append(a * b)
    elif op == "-":
        nums.append(a - b)
    elif op == "+":
        nums.append(a + b)


# Prints all 'print' statements by user in given sequence
def print_output():
    for output in outputs:
        print(output)


# Takes input from command line and calls functions to process or output it
# Driver Code
try:
    for input in sys.stdin:
        input = " ".join(input.split())
        if "print" in input:
            input = input.split(" ", 1)
            # TODO - handle validations
            output_vars = input[1].split(", ")
            output = ""
            for var in output_vars:
                output = f"{output} {state[var]}"
                outputs.append(output)
        else:
            input = input.split(" = ", 1)
            if len(input) == 1:
                # TODO - check if it is variable declaration and default it to 0 if value not provided. Otherwise, throw error
                pass
            elif len(input) == 2:
                state[input[0]] = evaluate(input[1])
    # Goes here with there is EOFError or KeyboardInterrupt
    print_output()

except Exception as e:
    # TODO - Check what all exceptions are to be handled
    print("Some error occurred. Please retry. Goodbye!", e)
