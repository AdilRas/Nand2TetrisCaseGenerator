from src.TestCaseGenerator import *

input_variables = [Var("a", 16, "B"), Var("b", 16, "B"), Var("sel", 1, "B")]
output_variables = [Var("out", 16, "B")]


# args = [a, b, sel]
# It is guaranteed that the input is 16 bits at most
def mux16_logic(args):
    a = args[0]
    b = args[1]
    sel = args[2]
    out = []
    out.append(args[16])
    return out


generate(name="Mux16", numCases=10, inVars=input_variables, outVars=output_variables, function=mux16_logic)


