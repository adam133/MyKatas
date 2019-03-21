#initialize a mapping for going from a roman numeral to digit, or back
RNMap = {'I':1,
             'V':5,
             'X':10,
             'L':50,
             'C':100,
             'D':500,
             'M':1000}
numMap = {1:'I',
             5:'V',
             10:'X',
             50:'L',
             100:'C',
             500:'D',
             1000:'M'}
#Setup a list of the numbers in order
#This is just for looping through possible options
divNumbers = [1,5,10,50,100,500,1000]

#Helper function to Rearrange RN that may be invalid with too many letters in a row.
def _makeValidRN(invalidRN):
    #Convert four repeating letters to their "correct" lettering
    invalidRN = invalidRN.replace('IIII','IV')
    invalidRN = invalidRN.replace('XXXX','XL')
    invalidRN = invalidRN.replace('CCCC','CD')
    #Convert ZYZ pattern to their "correct" lettering
    #9, 90, 900 patterns
    invalidRN = invalidRN.replace('VIV','IX')
    invalidRN = invalidRN.replace('LXL','XC')
    invalidRN = invalidRN.replace('DCD','CM')
    return invalidRN

#Helper function to Rearrange the RN into something easier to process
#this is a reverse of the _makeValidRN function
def _makeInValidRN(validRN):
    #Convert ZYZ pattern to their "incorrect" lettering
    #9, 90, 900 patterns
    validRN = validRN.replace('IX','VIV')
    validRN = validRN.replace('XC','LXL')
    validRN = validRN.replace('CM','DCD')
    #Convert 4's to 4 repeating letters
    validRN = validRN.replace('IV','IIII')
    validRN = validRN.replace('XL','XXXX')
    validRN = validRN.replace('CD','CCCC')
    return validRN

#Main function for converting a number to a Roman Numeral
#number should be a positive integer
def toRN(number):
    #Simplest case, input is directly mapped
    if number in numMap:
        return numMap[number]
    else:
        #loop through numbers, finding the next highest one.
        for i in reversed(divNumbers):
            if number/i >= 1:
                #subtract this amount
                number -= i
                #Then find the RN for the remainder
                #Concatenate that to the above letter
                #And send it all through the _makeValidRN function
                return _makeValidRN(numMap[i] + toRN(number))

#Main function for converting a Roman Numeral to Arabic
#instr should be a valid roman numeral
def toNum(instr):
    myTotal = 0
    if instr in RNMap:
        return RNMap[instr]
    else:
        #Run through the makeInvalidRN function
        myStr = _makeInValidRN(instr)
        #Take the first character, and add it to the total
        myTotal += RNMap[myStr[0]]
        #return the total added to the rest of the string
        return myTotal + toNum(myStr[1:])
        