import re
import sys

# Holds all outputs to print
outputs = []
# Holds latest values of variables
state = {}

# Evaluates any expression given


def evaluate(exp):

    for i in range(len(exp)):
        pass

    token_var = ""
    var_set = set()
    for x in range(len(exp)):
        if exp[x].isalpha():
            token_var += exp[x]
            if x == len(exp) - 1 or not exp[x + 1].isalpha():
                if token_var in state:
                    var_set.add(token_var)
                    token_var = ""
                elif token_var not in state:
                    state[token_var] = 0.0
                    var_set.add(token_var)
                    token_var = ""

    flag = True
    while flag == True:
        if "++" not in exp and "--" not in exp:
            flag = False
        last_index = 0
        while last_index < len(exp):
            for v in var_set:
                var = ""
                if exp[last_index:].startswith(v + "++"):

                    if len(exp) >= 3:
                        var = ""
                        for i, s in enumerate(exp):
                            if s.isalpha():
                                var += s
                                if (
                                    len(exp) >= i + 3
                                    and exp[i + 1] == "+"
                                    and exp[i + 2] == "+"
                                    and var != ""
                                ):
                                    if var in state:
                                        if "++" not in exp and "--" not in exp:
                                            flag = False
                                        exp = exp.replace(
                                            var, " " + str(state[var]) + " ", 1
                                        )
                                        state[var] += 1.0
                                        var = ""
                                        exp = exp.replace("++", "", 1)
                                        break
                                    else:
                                        state[var] = 0.0
                                        if "++" not in exp and "--" not in exp:
                                            flag = False
                                        exp = exp.replace(
                                            var, " " + str(state[var]) + " ", 1
                                        )
                                        state[var] += 1.0
                                        var = ""
                                        exp = exp.replace("++", "", 1)
                                        break

                    last_index += len(var) + 2
                    break

                elif exp[last_index:].startswith(v + "--"):
                    if len(exp) >= 3:
                        var = ""
                        for i, s in enumerate(exp):
                            if s.isalpha():
                                var += s
                                if (
                                    len(exp) >= i + 3
                                    and exp[i + 1] == "-"
                                    and exp[i + 2] == "-"
                                    and var != ""
                                ):
                                    if var in state:
                                        if "++" not in exp and "--" not in exp:
                                            flag = False
                                        exp = exp.replace(
                                            var, " " + str(state[var]) + " ", 1
                                        )
                                        state[var] -= 1.0
                                    else:
                                        state[var] = 0.0
                                        if "++" not in exp and "--" not in exp:
                                            flag = False
                                        exp = exp.replace(
                                            var, " " + str(state[var]) + " ", 1
                                        )
                                        state[var] -= 1.0
                                    var = ""
                        exp = exp.replace("--", "", 1)
                    last_index += len(var) + 2
                    break

                elif exp[last_index:].startswith("++" + v):
                    if exp[0] == "+" and exp[1] == "+":
                        for j in range(2, len(exp)):
                            if exp[j].isalpha():
                                var += exp[j]
                                if len(exp) > 3 and not exp[j + 1].isalpha():
                                    break
                        if var != "":
                            if var in state:
                                state[var] += 1.0
                                if "++" not in exp and "--" not in exp:
                                    flag = False
                                exp = exp.replace(
                                    var, " " + str(state[var]) + " ", 1)
                                var = ""
                            elif var not in state:
                                state[var] = 1.0
                                if "++" not in exp and "--" not in exp:
                                    flag = False
                                exp = exp.replace(
                                    var, " " + str(state[var]) + " ", 1)
                                var = ""
                        exp = exp[2:]
                        break

                    if len(exp) >= 3:
                        for i in range(len(exp)):
                            if (
                                exp[i - 2] in " /%*^-"
                                and exp[i - 1] == "+"
                                and exp[i] == "+"
                            ):
                                for j in range(i, len(exp)):
                                    if exp[j].isalpha():
                                        var += exp[j]
                                if var != "":
                                    if var in state:
                                        state[var] += 1.0
                                        if "++" not in exp and "--" not in exp:
                                            flag = False
                                        exp = exp.replace(
                                            var, " " + str(state[var]) + " ", 1
                                        )
                                        var = ""
                                        exp = exp.replace("++", "", 1)
                                        break
                                    elif var not in state:
                                        state[var] = 1.0
                                        if "++" not in exp and "--" not in exp:
                                            flag = False
                                        exp = exp.replace(
                                            var, " " + str(state[var]) + " ", 1
                                        )
                                        var = ""
                                        exp = exp.replace("++", "", 1)
                                        break

                    last_index += len(var) + 2
                    break

                elif exp[last_index:].startswith("--" + v):
                    if exp[0] == "-" and exp[1] == "-":
                        for j in range(2, len(exp)):
                            if exp[j].isalpha():
                                var += exp[j]
                                if len(exp) > 3 and not exp[j + 1].isalpha():
                                    break
                        if var != "":
                            if var in state:
                                state[var] -= 1.0
                                if "++" not in exp and "--" not in exp:
                                    flag = False
                                exp = exp.replace(
                                    var, " " + str(state[var]) + " ", 1)
                                var = ""
                            elif var not in state:
                                state[var] = -1.0
                                if "++" not in exp and "--" not in exp:
                                    flag = False
                                exp = exp.replace(
                                    var, " " + str(state[var]) + " ", 1)
                                var = ""
                        exp = exp[2:]
                        break

                    if len(exp) >= 3:
                        for i in range(len(exp)):
                            if (
                                exp[i - 2] in " /%*^+"
                                and exp[i - 1] == "-"
                                and exp[i] == "-"
                            ):
                                for j in range(i, len(exp)):
                                    if exp[j].isalpha():
                                        var += exp[j]
                                if var != "":
                                    if var in state:
                                        state[var] -= 1.0
                                        if "++" not in exp and "--" not in exp:
                                            flag = False
                                        exp = exp.replace(
                                            var, " " + str(state[var]) + " ", 1
                                        )
                                        var = ""
                                        exp = exp.replace("--", "", 1)
                                        break
                                    elif var not in state:
                                        state[var] = -1.0
                                        if "++" not in exp and "--" not in exp:
                                            flag = False
                                        exp = exp.replace(
                                            var, " " + str(state[var]) + " ", 1
                                        )
                                        var = ""
                                        exp = exp.replace("--", "", 1)
                                        break
                    last_index += len(var) + 2
                    break
            else:
                last_index += 1

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
    prev_char = None
    for s in string:
        # Checking if char encountered is a variable
        if s == " ":
            continue
        if s.isalpha():
            var_str += s
            continue
        if var_str in state:
            nums.append(state[var_str])
            var_str = ""
        elif var_str not in state and var_str != "":
            state[var_str] = 0.0
            nums.append(state[var_str])
            var_str = ""
        # Checking if char encountered is a number
        if s == "-" and (prev_char in ["(", None] or prev_char in "^/%*-+"):
            num_str += s
            continue
        # if s.lstrip('-').isdigit():
        #     num_str += "-"
        #     num_str += s
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
        prev_char = s
    if var_str in state:
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


# Driver Code - Takes input from command line and calls functions to process and output it
try:
    for input in sys.stdin:
        input = " ".join(input.split())
        if "print" in input:
            input = input.split(" ", 1)
            if len(input) == 2:
                output_vars = input[1].split(",")
                output = ""
                for var in output_vars:
                    var = var.strip()
                    space = " " if output else ""
                    if var in state:
                        output = f"{output}{space}{state[var]}"
                    elif var.isdigit():
                        output = f"{output}{space}{float(var)}"
                    elif var.isalpha():
                        # Not storing in state since we are printing and exiting
                        output = f"{output}{space}0.0"
                    else:
                        # +\-*/%^
                        match = re.search("[+|\-|*|/|%|^]", var)
                        if match is not None:
                            op = match.group()
                            exp = var.split(op)
                            # Ensure expression is valid
                            if len(exp) > 0:
                                output = f"{output}{space}{evaluate(var)}"
                outputs.append(output)
            else:
                # TODO - Handle case - user passes 'print' without any vars or wrong format
                pass
        else:
            temp_input = re.split("[+\-*/%^]=", input)
            if len(temp_input) == 2:
                op = input[input.index("=") - 1]
                lhs, rhs = temp_input[0].strip(), temp_input[1].strip()
                # Ignore cases where there is space in the middle anywhere in LHS since it is not valid
                if " " not in lhs:
                    state[lhs] = evaluate(f"{lhs} {op} {rhs}")
            # TODO - Implement compare extension and handle equal to case
            # elif '=' in input:
            #     # ==, <=, >=, !=, <, >
            #     match = re.search('==|<=|>=|!=|<|>]', var)
            #     if match is not None:
            #         com

            else:
                input = input.split("=", 1)
                if len(input) == 1 and ("++" in input[0] or "--" in input[0]):
                    op = "++" if "++" in input[0] else "--"
                    exp = input[0].split(op)
                    if len(exp) > 0:
                        lhs = exp[0] if exp[0] != "" else exp[1]
                        evaluate(input[0])
                    # if '++' in input[0]:
                    #     exp = input[0].split('++')
                    #     if len(exp) > 0 and exp[0] != '':
                    #         state[exp[0]] = evaluate(input[0])
                elif len(input) == 2:
                    lhs, rhs = input[0].strip(), input[1].strip()
                    # Ignore cases where there is space in the middle anywhere in LHS since it is not valid
                    if " " not in lhs:
                        state[lhs] = evaluate(rhs)

    # Goes here with there is EOFError or KeyboardInterrupt
    print_output()

except Exception as e:
    # TODO - Check what all exceptions are to be handled
    print("Some error occurred. Please retry. Goodbye!", e)
