这是一道再基本不过的题了，甚至被收录在 [stanford 的 cs 课件](http://cslibrary.stanford.edu/105/LinkedListProblems.pdf)里.

------

这道题最简单的思路就是利用归并排序的方法，因为每个链表本来就已经是内部有序了。
遍历两个链表，时间复杂度是O(n+m)，空间复杂度是O(1)。