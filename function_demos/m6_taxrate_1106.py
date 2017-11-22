# m6 examples tax rate

# current local tax rate
CURRENT_TAX_RATE = 0.085

def main():

    cost = float(input('Product cost? '))
    finalCost = cost + calc_tax(cost)
    print ('Cost with tax is:' ,finalCost)


def calc_tax(cost):
    """ calculates the current local tax
    base on the current tax rates """
    #return cost * 0.085
    tax = cost * CURRENT_TAX_RATE
    return tax



main()
    
