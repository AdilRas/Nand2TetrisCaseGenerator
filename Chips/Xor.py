from src.TestCaseGenerator import *

input_variables = [Var("a", 1, "B"), Var("b", 1, "B")]
output_variables = [Var("out", 1, "B")]


def xor_logic(args):
    out = []
    if args[0] == args[1]:
        out.append(0)
    else:
        out.append(1)
    return out


generate(name="Xor", numCases=10, inVars=input_variables, outVars=output_variables, function=xor_logic)


