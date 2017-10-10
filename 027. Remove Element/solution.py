class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        n = len(nums)-1
        i = 0
        while i <= n:
            if nums[i] == val:
                nums[i] = nums[n]
                n -= 1
            else:
                i += 1
        return n+1
    
    
if __name__ == '__main__':
    s = Solution()
    s.removeElement([3,2,3],3)