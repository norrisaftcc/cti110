# value returning function examples
# m6


def main():
    theNumber = int(input('Enter a number: '))
    showDouble(theNumber)

    anotherNumber = int(input('Enter another number: '))
    double = showDouble(anotherNumber)
    print("Double is:", double)



def showDouble(theNumber):
    """ double a number """
    doubledNumber = theNumber * 2
    print doubledNumber

                    

def findDouble(someNumber):
    """ double a number """
    doubledNumber = someNumber * 2
    return doubledNumber

main()
