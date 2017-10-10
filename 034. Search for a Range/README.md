这道题又是二分查找的变种。我因为时间有限，想出来的方法是最直接的。

首先先 init 一个 vector {-1,-1}, 这样如果没找到，直接返回无效值。

然后常规手法，二分查找，一旦找到，将 `vec[0] = vec[1] = mid`.

- 第一次二分，找到 target, 以及 start,end = iPos。
- 接着二分左边 nums[0, start], 以及右边 nums[end+1, n-1]。依然找 target.
- 不断循环往左、右二分查找 target，直到找不到为止。那么此刻范围也就确定好了。

这里题目中有个地方需要注意，题目中提到数组中全是整数。所以可以使用一种不一样的二分查找。
上面的二分查找是如果找不到就返回-1，其实可以将返回改成插入位置，然后分别查找target-0.5和target+0.5
这样直接找到范围，主要边界就行了。

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        left = self.binarySearch(nums, target - 0.5)
        right = self.binarySearch(nums, target + 0.5) - 1#!!
        
        if right < left:#!!
            return [-1, -1]
        
        return [left, right]
        
    def binarySearch(self, nums, target):
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
            
        return left
