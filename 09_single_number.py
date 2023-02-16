'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

https://leetcode.com/problems/single-number/

Note: This problem alongwith its constraints of not using extra space requires knowing bitwise operations 
which I personally think is too specific an area to know/remember off-hand. But it's still fun to brute 
force it while keeping more general space/memory constraints in mind. An xor solution is also provided.
Helpful things to keep in mind: 
1. N ^ N = 0
2. N ^ 0 = N
So if you xor everything against each other, eventually the unique number will XOR against zero and return itself
'''

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        count = dict()
        for n in nums:
            if n not in count:
                count[n] = 1
            else:
                count[n] = count[n] + 1
        for key, val in count.items():
            if val == 1:
                return key
        
    def singleNumberXOR(self, nums: list[int]) -> int:
        single = nums[0]
        for i in range(1,len(nums)):
            single = single ^ nums[i]
        return single


sol = Solution()
sol.singleNumberXOR([1,1,2,2,4])