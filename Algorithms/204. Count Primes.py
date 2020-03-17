'''
204. Count Primes

Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
'''

class Solution:
    def countPrimes(self, n: int) -> int:
        ans = []
        #to get number from 2 to num, for example, range(2,5) -> 2,3,4, range(2,6) -> 2,3,4,5
        for i in range(2, n+1):
            ct = 0
            #prime number only can divide by itself or one that's why no need to include itself
            for j in range(2,i):
                if i%j == 0:
                    ct += 1
            if ct ==0:
                ans.append(i)
        return len(ans)