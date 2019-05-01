# 输入一个链表，反转链表后，输出新链表的表头。
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        if pHead == None or pHead.next == None:
            return pHead
        pre = self.ReverseList(pHead.next)
        pHead.next.next = pHead
        pHead.next = None
        return pre


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
a.next = b
b.next = c
c.next = d
d.next = e
s = Solution()
print(s.ReverseList(a).next.val)

# class Solution:
#     # 返回ListNode
#     def ReverseList(self, pHead):
#         if pHead == None or pHead.next == None:
#             return pHead
#         pre = None
#         cur = pHead
#         while cur:
#             temp = cur.next
#             cur.next = pre
#             pre = cur
#             cur = temp
#         return pre