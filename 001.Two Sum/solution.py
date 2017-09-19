# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 11:10:32 2017

@author: yuanjun
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i,num in enumerate(nums):
            num2 = target-num
            j = nums[i+1:].index(num2)
            if j >=0:
                return [nums.index(num),nums.index(num2)]
            
if __name__ == '__main__':
    nums = [3,2,4]
    target = 6
    s = Solution()
    s.twoSum(nums,target)