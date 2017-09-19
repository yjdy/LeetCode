# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 11:10:32 2017

@author: yuanjun
"""

class Solution(object):
    def twoSum(self,nums, target):
        diction={}
        for i in range(len(nums)):
            if (target-nums[i] in diction) and diction[target-nums[i]]!=i:
                return [diction[target-nums[i]],i]
            diction[nums[i]]=i
        
if __name__ == '__main__':
    nums = [3,2,4]
    target = 6
    s = Solution()
    s.twoSum(nums,target)