C++解法暂缺

Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],
A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

3sum这题使用暴力求解不可取， 因为要得到所有解且考虑去重。
一个简单的方法是将数组排序，然后从小到大取一个数（至这个数大于0终止），这样问题就变成了在之后数组中的two sum问题。
这种解题方法时间复杂度是O(n^2+nlogn)，不过注意去重。
实测可过，不过较慢

代码中是目前的最优解，主要思想是先建立一个dict，key是nums中的值，内容是key出现的次数。
然后将key的正负区分出来成两个数组positives和negatives（注意0不会出现在negatives里，所以全0的情况要单列出来）
再组合positives和negatives里的值，查询剩余值是否能在dict里满足（存在？数量够？）来确定是否存在解。
这里说明一下，因为遍历的是key，已经去重了，不会出现重复情况。
时间复杂度是O(n^2+n)，没有order的区别，但是会快一些。
