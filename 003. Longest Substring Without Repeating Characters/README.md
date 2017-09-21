Given a string, find the length of the longest substring without repeating characters.
Examples:
Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

这道题的思想是当出现一个重复的字符时，重复字符之前的开始的子字符串都不可能了。
很明显的我们只需要考虑重复子字符串后开始的字符串，原本的长串会随着重复的出现而不断的截断，很明显的一个动态规划思想。

我们设置一个“指针”start，记录子字符串的开始位置，
随后我们遍历整个字符串，并设置一个dict记录出现的字符和出现的位置；借这个dict判断是否出现重复。
当出现重复时，先判断重复的位置是否在start之前，若是则不管；若不是，说明不重复子字符串已经到头了，判断长度是否为最长？
更新start，将start更改为重复字符的下一个，重复字符在dict中的值改为后一个值，继续遍历。
当剩余子串都不比最大子串长时就可以结束遍历了。

这里需要说明的是，python中下标运算远远慢于c，所以不要重复取下标而是考虑把具体值取出来。
如：for i,ch in enumerate(s):





