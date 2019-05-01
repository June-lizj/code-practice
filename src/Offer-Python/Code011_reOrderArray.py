# 输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
# 使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，
# 并保证奇数和奇数，偶数和偶数之间的相对位置不变。
class Solution:
    def reOrderArray(self, array):
        odd = filter(lambda num:num%2==1,array)
        even = filter(lambda num:num%2!=1,array)
        return list(odd)+list(even)

test = [1,-6,2,3,5,7,9,12,-7]
s = Solution()
print(s.reOrderArray(test))