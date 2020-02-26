from src.TestCaseGenerator import *

input_variables = [Var("in", 16, "B")]
output_variables = [Var("out", 16, "B")]


# args = [a]
# It is guaranteed that the input is 16 bits at most
def not16_logic(args):
    a = args[0]
    out = [(1 << 16) - a]
    return out


generate(name="Not16", numCases=10, inVars=input_variables, outVars=output_variables, function=not16_logic)


