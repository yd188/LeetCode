'''
The k-digit number N is an Armstrong number if and only if the k-th power of each digit sums to N.
Given a positive integer N, return true if and only if it is an Armstrong number.
Example 1:
Input: 153
Output: true
Explanation: 
153 is a 3-digit number, and 153 = 1^3 + 5^3 + 3^3.
Example 2:
Input: 123
Output: false
Explanation: 
123 is a 3-digit number, and 123 != 1^3 + 2^3 + 3^3 = 36.
Solution:
Find the least significant digit of a number by taking it modulus 10. 
Remove it by dividing the number by 10 (integer division).
Once you have a digit, you can raise it to the power of k and add it to the sum.
'''
def armstrongNumber(number):
    numberlen = len(str(number))
    finalNum = 0
    for num in [int(i) for i in str(number)]:
        finalNum += num**numberlen
    if finalNum == number:
        return True
    else:
        return False
