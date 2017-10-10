class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0: return 1
        if n < 0: return 1./self.myPow(x,-n)
        v = self.myPow(x,n/2)
        if n%2 == 0:
            return v*v
        else:
            return x*v*v
			
"""
def myPow(self, x, n):
    m = abs(n)
    ans = 1.0
    while m:
        if m & 1:
            ans *= x
        x *= x
        m >>= 1
    return ans if n >= 0 else 1 / ans
这种方法其实与上面的方法本质上是一样的，代价都是O(logn)
"""