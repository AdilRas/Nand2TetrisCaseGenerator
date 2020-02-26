from src.TestCaseGenerator import *

input_variables = [Var("a", 8, "B"), Var("b", 8, "B")]
output_variables = [Var("out", 1, "B")]


# args = [in, sel]
def or8way_logic(args):
    a = args[0]
    out = []
    if a > 0:
        out.append(1)
    else:
        out.append(0)
    return out



generate(name="Or4Way", numCases=10, inVars=input_variables, outVars=output_variables, function=or8way_logic)


