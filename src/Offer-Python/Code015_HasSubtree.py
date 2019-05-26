# 输入两棵二叉树A，B，判断B是不是A的子结构。
# ps：我们约定空树不是任意一个树的子结构
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        result = False
        if pRoot1 != None and pRoot2 != None:
            if pRoot1.val == pRoot2.val:
                result = self.HasSameSubstructure(pRoot1,pRoot2)
            if not result:
                result = self.HasSubtree(pRoot1.left,pRoot2)
            if not result:
                result = self.HasSubtree(pRoot1.right,pRoot2)
        return result

    def HasSameSubstructure(self,pRoot1,pRoot2):
        if pRoot2 == None:
            return True
        if pRoot1 == None:
            return False
        if pRoot1.val != pRoot2.val:
            return False
        return self.HasSameSubstructure(pRoot1.left,pRoot2.left) and self.HasSameSubstructure(pRoot1.right,pRoot2.right)

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
a.left = b
b.left = c
c.left = e
s = Solution()
print(s.HasSubtree(a,b))
print(s.HasSubtree(a,c))
print(s.HasSubtree(a,d))
print(s.HasSubtree(a,e))
