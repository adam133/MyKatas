import numberal

testNum = 0

#Test wrapper for Roman to Number
def runNumTest(expVal, inVal):
    global testNum
    testNum += 1
    retVal = numberal.toNum(inVal)
    if retVal != expVal:
        print("failed test " + str(testNum))
        print("expVal: " + str(expVal))
        print("inVal: " + str(inVal))
        print("retVal: " + str(retVal))
        raise ValueError
    elif retVal == expVal:
        print("pass test " + str(testNum))

expValLst = [1,5,10,50,100,500,1000]
inpValLst = ['I','V','X','L','C','D','M']

#simplest test - does a 1 = "I", 5="V"... etc
#first 7 tests
for i in inpValLst:
    runNumTest(expValLst[testNum], i)

print("End basic toNum test")

#no substraction needed, left to right, larger to smaller
#no 4's or 9's
runNumTest(8, 'VIII')
runNumTest(12, 'XII')
runNumTest(15, 'XV')
runNumTest(1002, 'MII')

print("End level 2 toNum tests")

#Ok... now try some ones with subtraction, 4's and 9's
runNumTest(49, 'XLIX')
runNumTest(9, 'IX')
runNumTest(99, 'XCIX')
runNumTest(89, 'LXXXIX')

print("End level 3 toNum tests")
