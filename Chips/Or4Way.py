from src.TestCaseGenerator import *

input_variables = [Var("a", 4, "B"), Var("b", 4, "B")]
output_variables = [Var("out", 1, "B")]


# args = [in, sel]
def or4way_logic(args):
    a = args[0]
    out = []
    if a > 0:
        out.append(1)
    else:
        out.append(0)
    return out



generate(name="Or4Way", numCases=10, inVars=input_variables, outVars=output_variables, function=or4way_logic)


