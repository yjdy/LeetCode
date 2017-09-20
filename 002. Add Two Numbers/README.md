You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8


链表类的题目一个比较常用的技巧是使用一个虚拟头结点，这样比较容易处理结尾的问题。
在这道题目的思路中其实可以用递归来解决，但是因为链表长度可能很长，导致递归占过大空间，所以不建议使用（实测oj也不过）
方法其实很简单，与笔算多位数加分是一样的，只是要注意好边界，尤其是最后的时候（一个为空，两个为空有进位等）
solution.py中采用了构建一个新列表来存储结果的方法，这种方法会带来内存和申请空间等开销，个人觉得比较好维护且不会更改原始数据。
oj上更快的代码思想是一样的，只是直接在原链表上进行修改，可以节省开销。