# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 11:10:32 2017

@author: yuanjun
"""

class Solution(object):
    def threeSum(self, nums):
        result, counter = [], {}
        for num in nums:
            if num not in counter:
                counter[num] = 0
            counter[num] += 1

        uniques = counter.keys()
        positives = [num for num in uniques if num >= 0]
        negatives = [num for num in uniques if num < 0]

        if 0 in counter and counter[0] > 2:
            result.append([0, 0, 0])#0不会出现在negatives里面，单独列出来

        for p in positives:#这里遍历的是key，已经去重了，不会出现重复情况
            for n in negatives:
                inverse = -(p + n)
                if inverse in counter:
                    if (inverse == p or inverse == n) and counter[inverse] > 1:
                        result.append([p, n, inverse])
                    elif inverse > p or inverse < n:
                        result.append([p, n, inverse])
        return result
        
if __name__ == '__main__':
    nums = [3,2,4]
    target = 6
    s = Solution()
    s.twoSum(nums,target)