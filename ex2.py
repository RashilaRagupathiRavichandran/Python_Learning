'''Write a Python function named max that takes a parameter containing a nonempty list of integers and returns the maximum value. (Note: there is a builtin function named max but pretend you cannot use it.)

'''
def avg(n):
    sum = 0
    for i in n:
        sum = sum + i
    return sum/len(n)

l1 = [1,2,3,4,5]
print(avg(l1))
