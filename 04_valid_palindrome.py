# Given a string s, return true if it is a palindrome, or false otherwise.
# https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        # List comprehension to remove special chars
        s = ''.join([i for i in s if i.isalnum()])
        # reverse the string by reading the same string backwards
        r = s[::-1]
        if r == s:
            return True
        return False