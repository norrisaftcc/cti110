# skeleton for M6LAB

def main():
    #print('not done')
    name = input('What is your name? ')
    greet(name)
    age = int(input('What is your age? '))
    print ('You are a: ', ageCategory(age))


def greet(name):
    """ greet user by name """
    print('Hello',name)



def ageCategory(age):
    # does not work yet!
    cat = 'infant'
    return cat  



# run program
main()
