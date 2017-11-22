# m6 examples
# 11/6

#name = 'DEFAULT USER'
GREETING_ENGLISH = 'Hello'
GREETING_FRENCH = 'Bonjour'
GREETING_GERMAN = 'Wilkommen'

#GREETING = GREETING_ENGLISH
GREETING = GREETING_FRENCH

def main():
    #global name
    print('welcome')
    name = input('what is your name? ')
    greet(name)
    function2()



def greet(name):
    """ Greet the user by name """
    print(GREETING, name)


def function2():
    print('in function2')



# start program
main()
