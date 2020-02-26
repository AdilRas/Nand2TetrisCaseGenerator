from src.TestCaseGenerator import *

input_variables = [Var("a", 1, "B"), Var("b", 1, "B")]
output_variables = [Var("out", 4, "B")]


# args = [a, b]
def or4_logic(args):
    a = args[0]
    b = args[1]
    out = []
    out.append(a | b)
    return out


generate(name="Or4", numCases=10, inVars=input_variables, outVars=output_variables, function=or4_logic)


