# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 14:22:35 2017

@author: yuanjun
"""

class Solution(object):
    def find_k_min_recursion(self,A,B,k):
        """
        每次递归都将当前的k减小约一半，这样时间复杂度是O(logk)；而这里k=(m+n)/2
        
        """
        if len(A)>len(B):#len(A)有可能比k/2小
            return self.find_k_min(B,A,k)
        if len(A) == 0:#不考虑A、B都为空的情况，这个为边界
            return B[k-1]
        if k == 1:
            return min(A[0],B[0])
        pa = min(k/2,len(A))#k/2>len(A)的情况
        pb = k-pa#k每次递归都能减少约一半
        if A[pa-1] < B[pb-1]:#有代码这里用<=，其实不影响结果；但是我倾向于写出==的情况，比较容易理解
            return self.find_k_min(A[pa:],B,pb)
        if A[pa-1] > B[pb-1]:
            return self.find_k_min(A,B[pb:],pa)
        if A[pa-1] == B[pb-1]:
            return A[pa-1]
    
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        length1 = len(nums1)
        length2 = len(nums2)
        if (length1+length2)%2==1:
            return self.find_k_min(nums1,nums2,(length2+length1)//2+1)
        else:
            return (self.find_k_min(nums1,nums2,(length1+length2)/2)+self.find_k_min(nums1,nums2,(length1+length2)/2+1))*0.5
        
    def find_k_min(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """ 
        length1 = len(nums1)
        length2 = len(nums2)
        if length1>length2:
            nums1,nums2 = nums2,nums1
            length1,length2 = length2,length1
        start1 = 0
        start2 = 0
        while length1-start1 > 0:
            if k == 1:
                return min(nums1[start1],nums2[start2])
            p1 = min(k//2,length1-start1)
            p2 = k-p1
            if nums1[p1-1+start1] < nums2[p2-1+start2]:
                start1 += p1
                k = p2
            elif nums1[p1-1+start1] > nums2[p2-1+start2]:
                start2 += p2
                k = p1
            elif nums1[p1-1+start1] == nums2[p2-1+start2]:
                return nums1[p1-1+start1]
            if length1-start1 > length2-start2:
                nums1,nums2 = nums2,nums1
                length1,length2 = length2,length1
                start1,start2 = start2,start1
        if length1-start1 == 0:
            return nums2[start2+k-1]
                
if __name__ == '__main__':
    s = Solution()
    print(s.findMedianSortedArrays([1,3],[2]))