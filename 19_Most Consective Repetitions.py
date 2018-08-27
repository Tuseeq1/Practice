# Question 8: Longest Repetition

# Define a procedure, longest_repetition, that takes as input a
# list, and returns the element in the list that has the most
# consecutive repetitions. If there are multiple elements that
# have the same number of longest repetitions, the result should
# be the one that appears first. If the input list is empty,
# it should return None.

def longest_repetition(li):
    if not li:
        return None

    element=''
    repetitions=0

    i=0
    while i<len(li)-1:
        cur_element=li[i]
        cur_repetition=1

        while li[i+1]==cur_element and i+1<len(li)-1:
            cur_repetition+=1
            i+=1

        if cur_repetition>repetitions:
            repetitions=cur_repetition
            element=cur_element
        i+=1

    return element





#For example,

print longest_repetition([1, 2, 2, 3, 3, 3, 2, 2, 1])
# 3

print longest_repetition(['a', 'b', 'b', 'b', 'c', 'd', 'd', 'd'])
# b

print longest_repetition([1,2,3,4,5])
# 1

print longest_repetition([])
# None
