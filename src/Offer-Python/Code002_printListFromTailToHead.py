# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# 输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3],返回[3,2,1]
    def printListFromTailToHead(self, listNode):
        if listNode is None:
            return []
        return self.printListFromTailToHead(listNode.next) + [listNode.val]

# 1.要进行输入非空检查
# 2.非空检查用is None,可能为空的对象不能调用方法或属性:listNode.val is None输入为空时报错
# 3.学会递归
# 4.list添加元素[] + [5] + [6]