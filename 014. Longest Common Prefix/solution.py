class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == None or len(strs) == 0:
            return ""

        prefix = strs[0]
        for s in strs:
            while not s.startswith(prefix):
                prefix = prefix[:-1]

        return prefix