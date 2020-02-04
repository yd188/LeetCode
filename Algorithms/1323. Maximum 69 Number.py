'''
1323. Maximum 69 Number

Given a positive integer num consisting only of digits 6 and 9.

Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).

 

Example 1:

Input: num = 9669
Output: 9969
Explanation: 
Changing the first digit results in 6669.
Changing the second digit results in 9969.
Changing the third digit results in 9699.
Changing the fourth digit results in 9666. 
The maximum number is 9969.
Example 2:

Input: num = 9996
Output: 9999
Explanation: Changing the last digit 6 to 9 results in the maximum number.
Example 3:

Input: num = 9999
Output: 9999
Explanation: It is better not to apply any change.
 

Constraints:

1 <= num <= 10^4
num's digits are 6 or 9.
'''

#Solution 1:
def maximum69Number(num):
    return str(num).replace('6', '9', 1)


#Solution 2:
def maximum69Number(num):
    str_num = str(num)
    if '6' in str_num:
        po = str_num.index('6')
        list_num = list(str_num)
        list_num[po] = '9'
        return ''.join(list_num)
    else:
        return None


#Solution 3:
def maximum69Number(num):
    str_num = str(num)
    ls = []
    for i in str_num:
        ls.append(i)
    for i in range(len(ls)):
        if ls[i] == '6':
            ls[i] = '9'
            break
        return ''.join(ls)
