# CODE TO GENERATE TEST CASES

import random


class Var:

    name: str       # x, y, in, etc
    length: int     # num bits (1, 4, 8, 16, etc)
    type: str       #
    lb: int         # the lower bound for the var
    ub: int         # the upper bound for the var
    cmp_len: int    # the field length for the cmp file

    def __init__(self, name, length, type, lower_bound=0, upper_bound=-1):
        self.name = name
        self.type = type
        self.length = length
        self.lb = lower_bound
        if upper_bound == -1:
            upper_bound = (1 << length) - 1
        self.ub = upper_bound
        self.cmp_len = max(len(name)+2, self.length+2)

    def __len__(self):
        return self.length

    def get_cmp_header(self):
        l = self.cmp_len - len(self.name)
        res = " " * (l // 2) + str(self.name) + " " * (l // 2)
        if l % 2 == 1:
            res += " "
        return res

    # It is assumed that len(value) == self.length
    def get_cmp_line(self, value):
        l = self.cmp_len - len(str(value))
        res = " " * (l // 2) + str(value) + " " * (l // 2)
        if l % 2 == 1:
            res += " "
        return res

    def get_tst_format(self):
        l = self.cmp_len - self.length
        leftSp = (l//2)
        rightSp = (l//2)
        if l % 2 == 1:
            rightSp += 1
        return self.name + "%" + self.type + str(leftSp) + "." + str(self.length) + "." + str(rightSp)


def printTstHeader(name, file, inVars, outVars):
    file.write("//" + name + ".tst\n\n")
    file.write( "load " + name + ".hdl,\n" +
                "output-file " + name + ".out,\n" +
                "compare-to " + name + ".cmp,\n" +
                "output-list ")
    output = []
    for var in inVars:
        output.append(var.get_tst_format())
    for var in outVars:
        output.append(var.get_tst_format())
    file.write(" ".join(output))
    file.write(";\n\n")


def printCmpHeader(file, inVars, outVars):
    outList = []
    for var in inVars:
        outList.append(var.get_cmp_header())
    for var in outVars:
        outList.append(var.get_cmp_header())
    file.write("|" + "|".join(outList) + "|\n")


def generateCases(num, inputs, rand=False):
    cases = []
    inpList = []
    if not rand:
        for i in range(num):
            # inputs for the passed in function
            inp = []
            # The current test case
            currCase = ""
            for var in inputs:
                inp.append(int(random.random() * (var.ub + 1)))
                currCase = currCase + "set " + var.name + " %" + var.type + str(bin(inp[-1])[2:].zfill(var.length)) + ",\n"
            currCase = currCase + "eval,\noutput;\n\n"
            cases.append(currCase)
            inpList.append(inp)
    else:
        numDigits = 0
        for var in inputs:
            numDigits += var.length
        n = min((1 << numDigits), num)
        for i in range(n):
            binNum = str(bin(i)[2:].zfill(16))
            inp = []
            currCase =  ""
            for j in range(len(inputs)):
                pass

    return cases, inpList


def printCases(file, caseText):
    for case in caseText:
        file.write(case)


def generateTstFile(name, caseText, inVars, outVars, directory):
    try:
        with open(directory+name+".tst", "w") as file:
            printTstHeader(name, file, inVars, outVars)
            printCases(file, caseText)
    except FileNotFoundError:
        print("Could not open or create file. Please check your filepath and try again: " + directory + name + ".tst")
    except:
        print("Error when opening file: " + directory + name + ".tst")


def evaluate(caseValues, function):
    results = []
    for case in caseValues:
        results.append(function(case))
    return results


def printCompares(file, inVars, outVars, caseValues, results):
    finalOuts = []
    for i in range(len(caseValues)):
        caseOut = []
        for j in range(len(inVars)):
            temp = inVars[j].get_cmp_line(bin(caseValues[i][j])[2:].zfill(inVars[j].length))
            caseOut.append(temp)
        for j in range(len(outVars)):
            temp = outVars[j].get_cmp_line(bin(results[i][j])[2:].zfill(outVars[j].length))
            caseOut.append(temp)
        finalOuts.append("|".join(caseOut))
    for line in finalOuts:
        file.write("|" + line + "|\n")


def generateCmpFile(name, caseValues, inVars, outVars, function, directory):
    try:
        with open(directory + name + ".cmp", "w") as file:
            printCmpHeader(file, inVars, outVars)
            results = evaluate(caseValues, function)
            printCompares(file, inVars, outVars, caseValues, results)
    except FileNotFoundError:
        print("Could not open or create file. Please check your filepath and try again: " + directory + name + ".cmp")
    except:
        print("Error when opening file: " + directory + name + ".cmp")



# This is the only function that should be called
def generate(name, numCases, inVars, outVars, function, directory=""):
    # Generate test data
    caseText, caseValues = generateCases(numCases, inVars)
    # Generate .tst
    generateTstFile(name, caseText, inVars, outVars, directory)
    # Generate .cmp
    generateCmpFile(name, caseValues, inVars, outVars, function, directory)


