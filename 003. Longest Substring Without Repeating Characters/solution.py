class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==0:
            return 0
        length = len(s)
        start=maxlen=0
        substr_dict= {}
        for i,ch in enumerate(s):
            if ch in substr_dict and start<=substr_dict[ch]:
                start = substr_dict[ch]+1
            else:
                maxlen = max(maxlen,i-start+1)
            substr_dict[ch]=i
            if length-start<=maxlen:
                break
        return maxlen