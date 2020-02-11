'''
7. Reverse Integer

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. 
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''

def reverse(x):
    flag = -1 if x < 0 else 1
    absnumber = abs(x)
    lastdigit = 0
    reversedigit = 0
    while absnumber:
        lastdigit = absnumber%10
        reversedigit = reversedigit*10 + lastdigit
        absnumber = int(absnumber/10)
    return reversedigit*flag
    
def reverse(x):
    flag = -1 if x < 0 else 1
    absnumber = abs(x)
    reversedigit = 0
    while absnumber:
        reversedigit = reversedigit*10 + absnumber%10
        absnumber = int(absnumber/10)
    return reversedigit*flag

def reverse(x):
    if x < 0:
        return int(str(x)[::-1][-1]+str(x)[::-1][:-1])
    elif str(x) == 0:
        return 0
    else:
        return int(str(x)[::-1])