import sys

# Holds all outputs to print
outputs = []
# Holds latest values of variables
state = {}

def evaluate(exp):
  # TODO - Merge code for evaluate here
  return exp

# Prints all 'print' statements by user in given sequence
def print_output():
  for output in outputs:
    print(output)

# Takes input from command line and calls functions to process or output it
try:
  for input in sys.stdin:
    input = ' '.join(input.split())
    if 'print' in input:
      input = input.split(' ', 1)
      # TODO - handle validations
      output_vars = input[1].split(', ')
      output = ''
      for var in output_vars:
        output = f'{output} {state[var]}'
      outputs.append(output)
    else:
      input = input.split(' = ', 1)
      if len(input) == 1:
        # TODO - check if it is variable declaration and default it to 0 if value not provided. Otherwise, throw error
        pass
      elif len(input) == 2:
        # TODO - handle spaces
        state[input[0]] = evaluate(input[1])
  # Goes here with there is EOFError or KeyboardInterrupt
  print_output()
except Exception as e:
  # TODO - Check what all exceptions are to be handled
  print("Some error occurred. Please retry. Goodbye!", e)