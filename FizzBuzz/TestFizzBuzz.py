#Test script for testing FizzBuzz.py
#starting with simple tests, going to more complex

import FizzBuzz

testNum = 0

#Test wrapper
def runTest(expVal, inNum):
    global testNum
    testNum += 1
    fb = FizzBuzz.FBgame()
    retVal = fb.play(inNum)
    if retVal != expVal:
        print("failed test " + str(testNum))
        print("expVal: " + expVal)
        print("inNum: " + str(inNum))
        print("retVal: " + retVal)
        raise ValueError
    elif retVal == expVal:
        print("pass test " + str(testNum))

#Test wrapper for custom games
def runCustomTest(fb, expVal, inNum):
    global testNum
    testNum += 1
    retVal = fb.play(inNum)
    if retVal != expVal:
        print("failed test " + str(testNum))
        print("expVal: " + expVal)
        print("inNum: " + str(inNum))
        print("retVal: " + retVal)
        raise ValueError
    elif retVal == expVal:
        print("pass test " + str(testNum))

#Test creation and returning normal value
runTest('1', 1)
runTest('29', 29)

#Test multiples of 3
runTest('fizz', 3)
runTest('fizz', 9)
runTest('fizz', 27)

#Test multiples of 5
runTest('buzz', 5)
runTest('buzz', 10)
runTest('buzz', 40)

#Test multiples of both 3 and 5
runTest('fizz buzz', 15)
runTest('fizz buzz', 45)

#Test multiples of 3,5, and 7
runTest('fizz buzz pop', 315)
runTest('fizz buzz pop', 105)

#Test creating/setting your own
fb = FizzBuzz.FBgame()
fb.setup(3, 'hoop')
fb.setup(2, 'spaghetti')
runCustomTest(fb, 'spaghetti hoop', 6)
runCustomTest(fb, '11', 11)
runCustomTest(fb, 'spaghetti hoop pop', 42)
fb.setup(11, 'zap')
runCustomTest(fb, 'spaghetti hoop pop zap', 462)
fb.setup(12, 'pow')
runCustomTest(fb, 'spaghetti hoop pop zap pow', 5544)

#Test a whole bunch of integers, see if there are any issues
print('printing output from numbers 1-100')
for i in range(1,101):
    print(fb.play(i))
