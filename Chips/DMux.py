from src.TestCaseGenerator import *

input_variables = [Var("in", 1, "B"), Var("sel", 1, "B")]
output_variables = [Var("a", 1, "B"), Var("b", 1, "B")]


# args = [in, sel]
def dmux_logic(args):
    a = args[0]
    b = args[1]
    sel = args[2]
    out = []
    if sel == 1:
        out.append(b)
    else:
        out.append(a)
    return out


generate(name="DMux", numCases=10, inVars=input_variables, outVars=output_variables, function=dmux_logic)


