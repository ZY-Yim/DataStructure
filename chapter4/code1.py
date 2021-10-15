# this file is about recursion

"""
Calculating the Sum of a List of Numbers
"""
def list_sum(num_list):
    """
    the_sum = 0

    for i in num_list:
        the_sum += i
    
    return the_sum
    """

    if len(num_list) == 1:
        return num_list[0]
    else:
        return num_list[0] + list_sum(num_list[1:])

print(list_sum([1, 3, 5, 7]))


"""
#### Converting an Integer to a String in Any Base
"""
def to_str(n, base):
    convert_string = "0123456789ABCDEF"
    if n < base:
        return convert_string[n]
    else:
        return to_str(n // base, base) + convert_string[n % base]

print(to_str(1453, 16))
print(to_str(10, 2))

"""
Stack Frames: Implementing Recursion
"""
import sys
sys.path.append(r"C:\Users\Yim\Documents\Python Scripts\DataStructure")
from chapter3.code1 import Stack

res = ""
r_stack = Stack()

def to_str_stack(n, base):
    convert_string = "0123456789ABCDEF"
    if n < base:
        r_stack.push(convert_string[n])
    else:
        r_stack.push(convert_string[n % base])
        to_str_stack(n // base, base)

to_str_stack(1453, 16)
# to_str_stack(10, 2)
while not r_stack.is_empty():
    res += r_stack.pop()
print(res)


