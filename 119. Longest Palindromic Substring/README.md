Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
Example: 
Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.

Example: 
Input: "cbbd"

Output: "bb"

C++解法暂缺

一个最直接的想法是利用最长公共子序列（LCS），将原字符串求反再求两者的LCS。
但是这个方法存在一个问题，即存在"abcdasdfghjkldcba"这样的情况（存在逆序子序列而不是回文序列），所以这种方法不行。

这道题的普通解法是遍历所有字符，验证：如果该字符是回文序列的中心那回文序列有多长（注意奇数、偶数两者情况）
这种解法的时间复杂度是O(n^2)，空间复杂度O(1); Python验证是否为回文序列其实很简单s==s[::-1]

然而存在着时间复杂度为O(n)的解法