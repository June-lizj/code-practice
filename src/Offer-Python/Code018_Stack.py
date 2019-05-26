# 定义栈的数据结构
# 请在该类型中实现一个能够得到栈中所含最小元素的min函数
# （时间复杂度应为O（1））。
class Solution:
    def __init__(self):
        self.arr = []
        self.assist = []
    def push(self, node):
        min = self.min()
        if not min or node < min:
            self.assist.append(node)
        else:
            self.assist.append(min)
        self.arr.append(node)
    def pop(self):
        # write code here
        if self.arr:
            self.assist.pop()
            return self.arr.pop()
    def top(self):
        # write code here
        if self.arr:
            return self.arr[-1]
    def min(self):
        # write code here
        if self.assist:
            return self.assist[-1]

# 1.除了添加元素，每一步都要进行非空检查
# 2.构造辅助栈帮助查找最小元素，
# 保证辅助栈的栈顶始终是最小的元素就可以实现一个时间复杂度为0（1）的min函数。
