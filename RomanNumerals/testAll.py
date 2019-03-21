import numberal

#Here's a true test, loop through all numbers 1 through 2000 
#making sure conversion to RN and back works fine for all numbers

for i in range(1, 2001):
    rn = numberal.toRN(i)
    #print(rn)
    mynum = numberal.toNum(rn)
    #print(mynum)
    if i != mynum:
        print("Problem with value: " + str(i))
        raise ValueError
print("done, no problems!")
