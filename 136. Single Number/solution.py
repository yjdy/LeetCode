class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for num in nums:
            result ^= num
        return result
    
if __name__ == '__main__':
    a = [1,2,4,2,1,5,4]
    s = Solution()
    res = s.singleNumber(a)
    print(res)
    