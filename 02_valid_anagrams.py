# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# https://leetcode.com/problems/valid-anagram/description/


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t) and sorted(s) == sorted(t):
            return True