这题最简单的方法是遍历整个列表用一个dict记录下遍历过的node
若发现有重复的node说明存在环，return True
若在发现重复node前遍历完(t == None)，那么说明没有环，return False
时间复杂度是O(n), 空间复杂度是O(n)。（python dict直接是hash dict，如果其他语言要考虑，因为其他种类的dict可能会超时）

若要空间复杂度为O(1),方法也很简单。就是设置连个pointer，一个步长为1遍历链表，一个步长为2遍历列表。
若出现追上的情况，则说明存在圈；若快pointer到达末尾说明不存在圈（注意因为步长为2，到达末尾的判断要考虑next和next.next）

return slow == fast