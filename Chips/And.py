from src.TestCaseGenerator import *
import pathlib
import os

input_variables = [Var("a", 1, "B"), Var("b", 1, "B")]
output_variables = [Var("out", 1, "B")]


def and_logic(args):
    out = []
    if args[0] == 1 and args[1] == 1:
        out.append(1)
    else:
        out.append(0)
    return out


generate(name="And", numCases=10, inVars=input_variables, outVars=output_variables, function=and_logic,
         directory=str(pathlib.Path(__file__).parent.parent / 'output') + os.sep
         )


