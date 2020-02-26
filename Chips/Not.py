from src.TestCaseGenerator import *

input_variables = [Var("in", 1, "B")]
output_variables = [Var("out", 1, "B")]


def not_logic(args):
    out = []
    if args[0] == 1:
        out.append(0)
    else:
        out.append(1)
    return out


generate(name="Not", numCases=10, inVars=input_variables, outVars=output_variables, function=not_logic)


