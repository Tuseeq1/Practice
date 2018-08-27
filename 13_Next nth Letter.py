# Write a procedure, shift_n_letters which takes as its input a lowercase
# letter, a-z, and an integer n, and returns the letter n steps in the
# alphabet after it. Note that 'a' follows 'z', and that n can be positive,
#negative or zero.

def shift_n_letters(letter, n):
    # converting into ascii code for easy addition
    asciiletter=ord(letter)
    newletter=asciiletter+n

    if newletter>122:
        newletter=96+(newletter-122)
    elif newletter<97:
        newletter=122-(96-newletter)

    return chr(newletter)

print shift_n_letters('s', 1)
#>>> t
print shift_n_letters('s', 2)
#>>> u
print shift_n_letters('s', 10)
#>>> c
print shift_n_letters('s', -10)
#>>> i
print shift_n_letters('z',1)
