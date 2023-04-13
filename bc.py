import sys

# Holds all outputs to print
outputs = []
# Holds latest values of variables
state = {}

increment_list = []
decrement_list = []

# Evaluates any expression given


def evaluate(exp):

    var = ""
    # ++x
    if exp[0] == "+" and exp[1] == "+":
        for j in range(2, len(exp)):
            if exp[j].isalpha():
                var += exp[j]
                if not exp[j + 1].isalpha():
                    break
        if var != "":
            if var in state:
                state[var] += 1.0
                var = ""
            elif var not in state:
                state[var] = 1.0
                var = ""
        exp = exp[2:]

    if len(exp) >= 3:
        for i in range(len(exp)):
            if exp[i - 2] in " /%*^-" and exp[i - 1] == "+" and exp[i] == "+":
                for j in range(i, len(exp)):
                    if exp[j].isalpha():
                        var += exp[j]
                if var != "":
                    if var in state:
                        state[var] += 1.0
                    elif var not in state:
                        state[var] = 1.0
                exp = exp[: i - 1] + " " + exp[i + 1:]
                i -= 1
            i += 1

    # --x
    if exp[0] == "-" and exp[1] == "-":
        for j in range(2, len(exp)):
            if exp[j].isalpha():
                var += exp[j]
                if not exp[j + 1].isalpha():
                    break
        if var != "":
            if var in state:
                state[var] -= 1.0
                var = ""
            elif var not in state:
                state[var] = -1.0
                var = ""
        exp = exp[2:]

    if len(exp) >= 3:
        for i in range(len(exp)):
            if exp[i - 2] in " /%*^+" and exp[i - 1] == "-" and exp[i] == "-":
                for j in range(i, len(exp)):
                    if exp[j].isalpha():
                        var += exp[j]
                if var != "":
                    if var in state:
                        state[var] -= 1.0
                    elif var not in state:
                        state[var] = -1.0
                exp = exp[: i - 1] + " " + exp[i + 1:]
                i -= 1
            i += 1
    # x++

    left_count = 0
    right_count = 0
    for e in exp:
        if e == "(":
            left_count += 1
        if e == ")":
            right_count += 1
    if left_count != right_count:
        return "parse error"

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
        if s == " ":
            continue
        if s.isalpha():
            var_str += s
            continue
        if var_str in state:
            if var_str in increment_list:
                state[var_str] += 1
                nums.append(state[var_str])
                increment_list.remove(var_str)
                var_str = ""
            elif var_str in decrement_list:
                state[var_str] -= 1
                nums.append(state[var_str])
                decrement_list.remove(var_str)
                var_str = ""
            else:
                nums.append(state[var_str])
                var_str = ""
        elif var_str not in state and var_str != "":
            state[var_str] = 0.0
            nums.append(state[var_str])
            var_str = ""
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
                    try:
                        apply_operation(nums, ops)
                    except IndexError:
                        return "parse error"
                    except ZeroDivisionError:
                        return "divide by zero"
                # Adding all operations to ops list
                ops.append(s)
    if var_str in state:
        if var_str in increment_list:
            state[var_str] += 1
            nums.append(state[var_str])
            increment_list.remove(var_str)
            var_str = ""
        elif var_str in decrement_list:
            state[var_str] -= 1
            nums.append(state[var_str])
            decrement_list.remove(var_str)
            var_str = ""
        else:
            nums.append(state[var_str])
            var_str = ""
    if var_str not in state and var_str != "":
        state[var_str] = 0.0
        nums.append(state[var_str])
        var_str = ""
    if num_str != "":
        nums.append(float(num_str))
    while ops:
        try:
            apply_operation(nums, ops)
        except IndexError:
            return "parse error"
        except ZeroDivisionError:
            return "divide by zero"
    # After all operations performed, return the only element left in the nums list
    return nums[0]


# this function helps decide which operation is performed first
def precedence(op):
    if op in "^":
        return 3
    elif op in "/%*":
        return 2
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


# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# for j in range(i, len(exp)):
#     if exp[j].isalpha():
#         var += exp[j]
# if var != "":
#     if var in state:
#         increment_list.append(var)
#     elif var not in state:
#         state[var] = 0.0
#         increment_list.append(var)
# exp = exp[: i - 1] + " " + exp[i + 1:]
# i -= 1
# i += 1
