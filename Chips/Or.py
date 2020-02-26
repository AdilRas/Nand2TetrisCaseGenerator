from src.TestCaseGenerator import *

input_variables = [Var("a", 1, "B"), Var("b", 1, "B")]
output_variables = [Var("out", 1, "B")]


def or_logic(args):
    out = []
    if args[0] == 1 or args[1] == 1:
        out.append(1)
    else:
        out.append(0)
    return out


generate(name="Or", numCases=10, inVars=input_variables, outVars=output_variables, function=or_logic)


