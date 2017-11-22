# m6 examples
# 11/6

name = 'DEFAULT USER'

def main():
    print('welcome')
    name = input('what is your name? ')
    greet(name)
    function2()



def greet(name):
    """ Greet the user by name """
    print('hello', name)


def function2():
    print('in function2')



# start program
main()
