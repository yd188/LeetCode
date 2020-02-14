'''
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4

http://laker.me/blog/2019/04/10/19_0410_leetcode136/

'''
def findSignleNum(nums):
    rst = 0
    for i in nums:
        rst^=i
    return rst

def signleNumber(nums):
    if len(nums) == 1:
        return nums[0]
    else:
        numsdict = {i:nums.count(i) for i in nums}
        keys = list(numsdict.keys())
        values = list(numsdict.values())
        return keys[values.index(min(numsdict.values()))]

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        lt = []
        for i in nums:
            if i in lt:
                lt.remove(i)
            else:
                lt.append(i)
        return lt.pop()
        
#Approach 1 - Array

def singleNumber1(nums):
    list = []
    for i in nums:
        if i in list:
            list.remove(i)
        else:
            list.append(i)
    return list.pop()
'''
Use array(in Python called list) to store numbers in nums. If some number in nums is new to array, append it.If some number is already in the array, remove it

Time complexity : O(n^2). for i in nums takes O(n) time, and if i in list is also a for-loop taking O(n) time.
Space complexity : O(n). We need a list of size n to contain elements in nums.
Approach 2 - Hash
'''

def singleNumber2(nums):
    dict = {}
    for i in nums:
        if dict.has_key(i):
            dict.pop(i)
        else:
            dict.update({i: 0})
    print dict
    for key, val in dict.items():
        if val == 0:
            return key

def singleNumber5(nums):
    hash_table = {}
    for i in nums:
        try:
            hash_table.pop(i)
        except:
            hash_table[i] = 1
    # popitem(): Remove the last item from the dictionary:
    return hash_table.popitem()[0]

'''
Use array(in Python called list) to store numbers in nums. If some number in nums is new to array, append it.If some number is already in the array, remove it

Time complexity : O(n). for i in nums takes O(n) time, and if dict.has_key(i) takes O(1) time.
Space complexity : O(n). We need a hash table of size n to contain elements in nums.
Approach 3: Math
'''

def singleNumber3(nums):
    # sum(a)
    # a is the list , it adds up all the numbers in the
    # list a and takes start to be 0, so returning
    # only the sum of the numbers in the list.
    # sum(a, start)
    # this returns the sum of the list + start
    # set(list): remove the duplicate
    return 2 * sum(set(nums)) - sum(nums)
    
'''
2^(a+b+c)−(2a+2b+c)=c

Time complexity : O(n + n) = O(2n)=O(n). sum() is a for-loop.
Space complexity : O(n + n) = O(2n)=O(n). A set needs space for the elements in nums
Approach 4: XOR
Because a^0=a and a^a=0
Then: a^b^a=(a^a)^b=0^b=b
So we can XOR all bits together to find the unique number.
'''

def singleNumber4(nums):
    a = 0
    for i in nums:
        a ^= i
    return a
