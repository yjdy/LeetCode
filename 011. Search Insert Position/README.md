简单的二分搜索题
二分搜索的关键在于找**中点(mid)**, 然后两头保持一个 low 和一个 high两个标记. 
```cpp
if (A[mid] == target) return mid;
else if (A[mid] < target) low = mid + 1;
else high = mid - 1; // A[mid] > target.
```

上述三个判断, 就是二分搜索的核心了.复习一下基础算法. 很有必要.


