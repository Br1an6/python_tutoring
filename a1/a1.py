# A-1 learn basics and conditions
import math

def getSideC():
    """
       /|
    x / | 4
     /__|
      3

    x = math.sqrt(9+16)
    >>> getSideC()
    5
    """
    side_a = 3
    side_b = 4
    side_c = 0

    # TODO: print of the value for side c
    # side_c = math.sqrt(put_number_here) # use this to get the square root 


    print "Side c is:", side_c


def printPosOrNeg(num):
    """ 
    look at the print above. Use if and else.
    print "is positive"
    print "is negative"
    """
    # TODO: write if and else to print
    pass # remove me


def main():
    """ Main method"""
    print "===This is A-1==="
    print "=======Your output======"
    print "[*] Part 1 getSideC output: "
    getSideC() # should print 5
    print "\n"
    print "[*] Part 2 printPosOrNeg output: "
    for num in [1, -1, 2, 4]:
        print "input ", num, " is :"
        printPosOrNeg(num)
    print "==========Done=========="
    print "\n\n"
    print "==========Answer========"
    print "p1: 5  p2: is positive, is negative, is positive, is positive"


if __name__ == '__main__':
    main()