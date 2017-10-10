
在线性数组中，删除某元素，乍一想免不了要移动大量元素了，但题中却给了这么一句话：
> The order of elements can be changed. It doesn't matter what you leave beyond the new length.

我一下子就明白了题目的意图。超出长度的部分是废弃的，那么我就可以把重复的元素和这些废弃的部分交换了，再等等，连交换都多余，
其实只需要将**超出长度的部分中不等于要寻找的那个值的元素填充到前面重复元素的位置即可**。

够啰嗦么？ 费了半天劲AC之后，我才开始反思这段代码，发现 `discard` 其实没必要存在，因为参数中有一个 `n` 可以利用。
然后，这时恰好和 @Mooophy 讨论了不完整 `for` 语句的妙用，顿时发现自己一个思维漏洞：len 为啥要每次++ ？这造成了我中间不必要的判断。

写出这样的代码，其实代表着一种思维的混乱，或说被语法所束缚，没有放开思路。

-----

我重新考虑了这个问题最本质的思路，改写如下：

```cpp
int removeElement(int A[], int n, int elem) {//这里没有i++，这样可以避免很多不必要的判断
    for (int i = 0; i < n;)
    {
        if (A[i] == elem) A[i] = A[--n];
        else ++i;
    }
    return n;
}
```

Python 的for循环里：
for item in nums:
    if item == val:
        nums.remove(item)
#nums=[3,2,3],val=3
#没有出现item=2的情况，直接到item=3
#而且如果nums=[3,3,3]，则第2个3会保留下来！！
下一个item是当前item的下一个元素，如果当前元素被删除则当前元素会变成下一个元素，所以下一个遍历的元素将是下下个元素（即下一个元素不会被遍历）
感觉还是利用下标在遍历一样
