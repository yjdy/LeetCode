class Solution(object):
    def longestPalindrome(self, s):
        if len(s)==0:
        	return 0
        maxLen=1
        start=0
        for i in xrange(len(s)):#假设某字符为回文序列中心找最长的回文序列
        	if i-maxLen >=1 and s[i-maxLen-1:i+1]==s[i-maxLen-1:i+1][::-1]:#s[i]为中心奇数长度序列
        		start=i-maxLen-1
        		maxLen+=2
        		continue

        	if i-maxLen >=0 and s[i-maxLen:i+1]==s[i-maxLen:i+1][::-1]:#s[i]为中心偶数长度序列
        		start=i-maxLen
        		maxLen+=1
        return s[start:start+maxLen]
    
if __name__ == '__main__':
    s = Solution()
    print s.longestPalindrome("abcdasdfghjkldcba")