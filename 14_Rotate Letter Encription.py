# Write a procedure, rotate which takes as its input a string of lower case
# letters, a-z, and spaces, and an integer n, and returns the string constructed
# by shifting each of the letters n steps, and leaving the spaces unchanged.
# Note that 'a' follows 'z'. You can use an additional procedure if you
# choose to as long as rotate returns the correct string.
# Note that n can be positive, negative or zero.

def rotate(string, number):
    newstring=''
    for letter in string:
        if 'a'<=letter<='z':
            asciiletter=ord(letter)
            newletter=asciiletter+number

            if newletter>122:
                newletter=96+(newletter-122)
            elif newletter<97:
                newletter=122-(96-newletter)
            newstring+=chr(newletter)
        else:
            newstring+=letter
    return newstring

print rotate ('sarah', 13)
#>>> 'fnenu'
print rotate('fnenu',13)
#>>> 'sarah'
print rotate('dave',5)
#>>>'ifaj'
print rotate('ifaj',-5)
#>>>'dave'
print rotate(("zw pfli tfuv nfibj tfiivtkcp pfl jyflcu "
                "sv rscv kf ivru kyzj"),-17)
#>>> ???
