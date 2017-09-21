Reverse digits of an integer.
Example1: x = 123, return 321
Example2: x = -123, return -321 
click to show spoilers.
Note:
The input is assumed to be a 32-bit signed integer. Your function should return 0 when the reversed integer overflows. 

最直观的想法是使用求余的方法一位一位的翻转数字，这种方法需要考虑好几个特殊的边界：
1.原数字为0；2.原数为负时要取绝对值，最后结果再乘以-1；3原数字结尾为0时，不要出现在翻转数字的开头。

但是在python中存在更简单快捷的方法，直接将原数字变成字符串再字符串翻转y[::-1]
注意开头的负号就行。比求余的方法更快更简单；不过c\c++里结果不一定，需要测试一下。
