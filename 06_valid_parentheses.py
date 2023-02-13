'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

https://leetcode.com/problems/valid-parentheses/description/
'''

from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            # odd len of string will never be true
            return False
        stack = deque()
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            if c == ')' or c == '}' or c == ']':
                if len(stack) > 0:
                    pop = stack.pop()
                else:
                    return False
                if c == ')' and pop != '(':
                    return False
                elif c == '}' and pop != '{':
                    return False
                elif c == ']' and pop != '[':
                    return False
        # loop is over, the whole string is finished, 
        # no open brackets should remain, stack len should be zero
        if len(stack) > 0:
            return False
        return True