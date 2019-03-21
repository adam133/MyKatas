import numberal

testNum = 0

#wrapper for running tests
def runRNTest(expVal, inVal):
    global testNum
    testNum += 1
    retVal = numberal.toRN(inVal)
    if retVal != expVal:
        print("failed test " + str(testNum))
        print("expVal: " + str(expVal))
        print("inVal: " + str(inVal))
        print("retVal: " + str(retVal))
        raise ValueError
    elif retVal == expVal:
        print("pass test " + str(testNum))

expValLst = ['I','V','X','L','C','D','M']
inpValLst = [1,5,10,50,100,500,1000]

#simplest test - does a 1 = "I", 5="V"... etc
#first 7 tests
for i in inpValLst:
    runRNTest(expValLst[testNum], i)

print("End basic RN test")

#no substraction needed, left to right, larger to smaller
#no 4's or 9's
runRNTest('VIII', 8)
runRNTest('XII', 12)
runRNTest('XV', 15)
runRNTest('MII', 1002)

print("End level 2 RN tests")

#Ok... now try some ones with subtraction, 4's and 9's.
runRNTest('XLIX', 49)
runRNTest('IX', 9)
runRNTest('XCIX', 99)
runRNTest('LXXXIX', 89)

print("End level 3 RN tests")

