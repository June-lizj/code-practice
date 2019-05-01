# 输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        return

a = ListNode(1)
b = ListNode(3)
c = ListNode(5)
d = ListNode(2)
e = ListNode(4)
f = ListNode(6)
a.next = b
b.next = c
d.next = e
e.next = f

s = Solution()
print(s.Merge(a,d).next.val)

# 1.考虑输入为空
# 2.链表迭代方式:result=result.next
# 3.如何迭代链表的同时最后输入头结点:用一个临时变量存储头结点
# 4.考虑当一个链表迭代结束后另一个链表还有剩余的情况
# 5.考虑递归实现

# class Solution:
#     # 返回合并后列表
#     def Merge(self, pHead1, pHead2):
#         result = ListNode(0)
#         temp = result
#         if pHead1 == None:
#             return pHead2
#         if pHead2 == None:
#             return pHead1
#         while pHead1 or pHead2:
#             if pHead1.val > pHead2.val:
#                 result.next = pHead2
#                 pHead2 = pHead2.next
#             else:
#                 result.next = pHead1
#                 pHead1 = pHead1.next
#             result = result.next
#         if pHead1:
#             result.next = pHead1
#         elif pHead2:
#             result.next = pHead2
#         return temp.next