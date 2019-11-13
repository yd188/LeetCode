'''
1180.Count Substrings with Only One Distinct Letter

Example 1:

Input: S = 'aaaba'
Output: 8
Explanation: The substrings with one distinct letter are 'aaa', 'aa', 'a', 'b'.
'aaa' occurs 1 time.
'aa' occurs 2 times.
'a' occurs 4 times.
'b' occurs 1 time.
So the answer is 1 + 2 + 4 + 1 = 8.
Example 2:

Input: S = 'aaaaaaaaaa'
Output: 55
'''

def countSubstr(S):
    result = len(S)
    left = 0
    for right in range(1,len(S)):
        if S[right]==S[left]:
            result += right - left
        else:
            left = right
    return result
