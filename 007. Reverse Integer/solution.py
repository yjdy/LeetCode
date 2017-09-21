class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x>=0:
            flag = 1
            y = str(x)
        else:
            flag = -1
            y = str(x)[1:]
        y = int(y[::-1])*flag
        if y>2**31-1 or y<-2**31:
            return 0
        else:
            return y