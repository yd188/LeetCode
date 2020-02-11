'''
1021. Remove Outermost Parentheses

A valid parentheses string is either empty (""), "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.  For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.

A valid parentheses string S is primitive if it is nonempty, and there does not exist a way to split it into S = A+B, with A and B nonempty valid parentheses strings.

Given a valid parentheses string S, consider its primitive decomposition: S = P_1 + P_2 + ... + P_k, where P_i are primitive valid parentheses strings.

Return S after removing the outermost parentheses of every primitive string in the primitive decomposition of S.

 

Example 1:

Input: "(()())(())"
Output: "()()()"
Explanation: 
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()".
Example 2:

Input: "(()())(())(()(()))"
Output: "()()()()(())"
Explanation: 
The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".
Example 3:

Input: "()()"
Output: ""
Explanation: 
The input string is "()()", with primitive decomposition "()" + "()".
After removing outer parentheses of each part, this is "" + "" = "".
 

Note:

S.length <= 10000
S[i] is "(" or ")"
S is a valid parentheses string
'''

def removeOuterParentheses(S):
    s = list(S)
    balance = 0
    for i in range(len(s)):
        balance += 1 if s[i] == ')' else -1
        if balance == 0:
            s[i] = ''
            try:
                s[i+1]=''
            except:
                pass
    s[0]=''
    return ''.join(s)

def removeOuterParentheses(S):
    s = list(S)
    count = 0
    for i, string in enumerate(s):
        count += 1 if string == ')' else -1
        if count == 0:
            s[i] = ''
            try:
                s[i+1] = ''
            except:
                pass
    s[0] = ''
    return ''.join(s)

#when count = 0 remove first '(' and last ')'
def removeOuterParentheses(S):
    previousi = 0
    res = ''
    count = 0
    for i, s in enumerate(S):
        count += 1 if s == '(' else -1
        if count == 0:
            res += S[previousi+1:i]
            previousi = i+1
    return res    
    
class Solution:
    def removeOuterParentheses(S):
        previ = 0
        res = ""
        count = 0
        for i, s in enumerate(S):
            if s == '(':
                count += 1
            else:
                count -= 1
            if count == 0:
                res += S[previ + 1: i]
                previ = i + 1
        return res