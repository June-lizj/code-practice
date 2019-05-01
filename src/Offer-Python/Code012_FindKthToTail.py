# 输入一个链表，输出该链表中倒数第k个结点。

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        if head == None:
            return None
        kthNode = head
        while head.next != None:
            head = head.next
            if k == 1:
                kthNode = kthNode.next
            else:
                k -= 1
        if k != 1:
            return None
        return kthNode


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
print(s.FindKthToTail(a,7).val)

# 1.输入节点为空
# 2.k的值大于链表节点数
# 3.k为0或负数