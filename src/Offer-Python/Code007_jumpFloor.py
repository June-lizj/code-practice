# 一只青蛙一次可以跳上1级台阶，也可以跳上2级。
# 求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
class Solution:
    def jumpFloor(self, number):
        if number <= 0:
            return 0
        result = [0,1,2]
        while len(result) < number +1:
            result.append(result[-2]+result[-1])
        return result[number]

s = Solution()
print(s.jumpFloor(3))

# 1.最后一跳为1阶或2阶,所以问题可分解为F(n)=F(n-1)+F(n-2)斐波那契数列
# 2.注意直接递归可能超时