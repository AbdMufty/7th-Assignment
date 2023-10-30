#import copy
def chop(x):
    #y = copy.copy(x)
    #del y[0]
    #del y [-1]
    #return y
    del x[0]
    del x[-1]

def middle (x):
    l = len(x)-1
    y = x[1:l]
    return y

num1 = [1,2,3,4]
num2 = [1,2,3,4]

print("My list before calling the chop function",num1)
chop(num1)
print("My list after calling the chop function",num1)

print("\nMy list before calling the middle function",num2)
middle(num2)
new_list = middle(num2)
print("My list after calling the middle function",num2)
print("New list after calling the middle function",new_list)