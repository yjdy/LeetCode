# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 11:10:32 2017

@author: yuanjun
"""

from collections import Counter
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <3:
            return []
        res = []
        d = Counter(nums)
        positives = [key for key in d if key >=0]
        negatives = [key for key in d if key < 0]
        if d[0]>=3:
            res.append([0,0,0])
        for p in positives:
            for n in negatives:
                inverse = -(p+n)
                if inverse in d:
                    if (inverse == p or inverse ==n) and d[inverse]>1:
                        res.append([p,n,inverse])
                    elif inverse >p or inverse <n:
                        res.append([p,n,inverse])
        return res
        
if __name__ == '__main__':
    nums = [-1,0,1,2,-1,-4]
    s = Solution()
    s.threeSum(nums)