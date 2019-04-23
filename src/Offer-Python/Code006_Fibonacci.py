# 大家都知道斐波那契数列，现在要求输入一个整数n，
# 请你输出斐波那契数列的第n项（从0开始，第0项为0）。
# n<=39
class Solution:
    def Fibonacci(self, n):
        result = [0,1]
        if n < 2:
            return result[n]
        # for i in range(2,n+1):
        #     result.append(result[i-1]+result[i-2])
        while len(result) < n+1:
            result.append(result[-1]+result[-2])
        return result[n]

s = Solution()
print(s.Fibonacci(6))

# class Solution:
#     def Fibonacci(self, n):
#         if n < 2:
#             return n
#         return self.Fibonacci(n - 1) + self.Fibonacci(n - 2)
# Fibonacci(4) = Fibonacci(3) + Fibonacci(2);
#                     = Fibonacci(2) + Fibonacci(1) + Fibonacci(1) + Fibonacci(0);
#                     = Fibonacci(1) + Fibonacci(0) + Fibonacci(1) + Fibonacci(1) + Fibonacci(0);
# 简单递归重复计算严重,n稍微大一点就会花很多时间