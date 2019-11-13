'''
Given a string S, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.

 
Example 1:

Input: 'leetcodeisacommunityforcoders'
Output: 'ltcdscmmntyfrcdrs'
Example 2:

Input: 'aeiou'
Output: ''
 

Note:

S consists of lowercase English letters only.
1 <= S.length <= 1000
'''

def removeVowels(st):
    rst =''
    vowels = {'a', 'e', 'i', 'o', 'u'}
    for s in st:
        if s not in vowels: 
            rst += s
    return rst
