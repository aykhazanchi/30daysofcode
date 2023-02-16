'''
You are given a large integer represented as an integer array digits, where each digits[i] 
is the ith digit of the integer. The digits are ordered from most significant to least 
significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

https://leetcode.com/problems/plus-one/
'''
class Solution:
    # Faster but not as memory-efficient
    def plusOne(self, digits: list[int]) -> list[int]:
        o_str = ''
        for d in digits:
            o_str += str(d)
        n_str = str(int(o_str) + 1)
        return [int(n) for n in n_str]

    # beats LC 95% on memory
    def plusOneMem(self, digits: list[int]) -> list[int]:
        o_str = ''
        for d in digits:
            o_str += str(d)
        n_num = int(o_str) + 1
        n_str = str(n_num)
        n_arr = []
        for n in n_str:
            n_arr.append(n)
        return n_arr
