class FBgame:
    #Initialize the fizz buzz game
    def __init__(self):
        #set the default divisors/words
        self.divisors = dict([
                            (3, 'fizz'), 
                            (5, 'buzz'),
                            (7, 'pop')])
    
    #function for setting your own fizz/buzz combo on an already existing FBgame object
    #divisor should be a positive integer
    #word should be a string
    def setup(self, divisor, word):
        self.divisors[divisor] = word
        
    #Main game function
    #num should be a positive integer
    def play(self, num):
        #init these variables
        mystr = ''
        #Loop through the divisors in sorted order
        #sorted to make sure the printed string is always the same order
        for k, v in sorted(self.divisors.items()):
            #check if its a match with modulo
            if num % k == 0:
                #add a space if there is already 1 or more matches
                if len(mystr) > 0:
                    mystr = mystr + ' '
                #Add the string
                mystr = mystr + self.divisors[k]
        #return the appropriate string
        if len(mystr) == 0:
            return str(num)
        else:
            return mystr