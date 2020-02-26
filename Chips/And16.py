from src.TestCaseGenerator import *

input_variables = [Var("a", 16, "B"), Var("b", 16, "B")]
output_variables = [Var("out", 16, "B")]


# args = [a]
# It is guaranteed that the input is 16 bits at most
def and16_logic(args):
    a = args[0]
    b = args[1]
    out = []
    out.append(a & b)
    return out


generate(name="And16", numCases=10, inVars=input_variables, outVars=output_variables, function=and16_logic)


