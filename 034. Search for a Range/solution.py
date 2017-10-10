class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = [-1,-1]
        if not nums:
            return result
        index = self.binarySearch(nums,target)
        if index < 0:
            return result
        start = index
        end = index
        while True:
            temp_start = self.binarySearch(nums[0:start],target)
            if temp_start < 0:
                break
            if temp_start < start:
                start = temp_start
        while True:
            temp_end = self.binarySearch(nums[end+1:len(nums)],target)
            if temp_end < 0:
                break
            if temp_end >= 0:
                end += temp_end+1
        return [start,end]
    
    def binarySearch(self,nums,target):
        if not nums:
            return -1
        start,end = 0,len(nums)-1
        while start<=end:
            mediate = (start+end)/2
            m = nums[mediate]
            if m == target:
                return mediate
            elif m > target:
                end = mediate-1#查过的不要再进入查询范围否则容易死循环
            else:
                start = mediate+1
        return -1
    
if __name__ == '__main__':
    s = Solution()
    print s.searchRange([2,2],2)