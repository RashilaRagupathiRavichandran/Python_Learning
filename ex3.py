'''Write a Python function named max that takes a parameter containing a nonempty list of integers and returns the maximum value. (Note: there is a builtin function named max but pretend you cannot use it.)
'''
def max(n):
    max = 0
    for i in n:
        if i > max:
            max = i
    return max

l1 = [11,12,33,4,5]
print(max(l1))

