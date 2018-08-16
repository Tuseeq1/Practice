# Define a procedure, print_multiplication_table,
# that takes as input a positive whole number, and prints out a multiplication,
# table showing all the whole number multiplications up to and including the
# input number. The order in which the equations are printed matters.

def print_multiplication_table( n ):
    # your code goes here
    if n%1==0 and n>=0:
        for number in range(1,n+1):
            for multiples in range(1,n+1):
                print '>>> '+str(number)+' * '+' '+str(multiples)+' = '+str(number*multiples)
    else:
        print "Error: Not a positive whole number."




print_multiplication_table(0)
#>>> 1 * 1 = 1
#>>> 1 * 2 = 2
#>>> 2 * 1 = 2
#>>> 2 * 2 = 4

print_multiplication_table(3)
#>>> 1 * 1 = 1
#>>> 1 * 2 = 2
#>>> 1 * 3 = 3
#>>> 2 * 1 = 2
#>>> 2 * 2 = 4
#>>> 2 * 3 = 6
#>>> 3 * 1 = 3
#>>> 3 * 2 = 6
#>>> 3 * 3 = 9
