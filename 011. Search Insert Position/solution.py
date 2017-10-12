class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        start = 0
        end = len(nums)-1
        while start <= end:
            mid = (start+end)/2
            temp = nums[mid]
            if temp == target:
                return mid
            elif temp > target:
                end = mid-1
            else:
                start = mid+1
        return start
