# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashTable = dict()
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashTable:
                return [i, hashTable[diff]]
            hashTable[nums[i]] = i