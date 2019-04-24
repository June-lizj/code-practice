# 一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。
# 求该青蛙跳上一个n级的台阶总共有多少种跳法。
class Solution:
    def jumpFloorII(self, number):
        if number < 0:
            return -1
        if number == 0:
            return 0
        return 2**(number-1)
s = Solution()
print(s.jumpFloorII(4))

# 1.写出公式进行推导,找规律
# 2.每个台阶都有跳与不跳两种可能,最后一个台阶必跳,所以是2^(n-1)
# 3.顺着上一题的思路,最后一跳
# f(n)=f(n-1)+f(n-2)+......+f(n-n)
#     =f(0)+f(1)+......+f(n-2)+f(n-1)
# f(n-1)=f(0)+f(1)+....+f(n-2)
# f(n)=f(n-1)+f(n-1)
#     =2*f(n-1)

# class Solution:
#     def jumpFloorII(self, number):
#         if number < 0:
#             return -1
#         if number == 1:
#             return 1
#         return 2*self.jumpFloorII(number-1)

# class Solution:
#     def jumpFloorII(self, number):
#         if number < 0:
#             return -1
#         result = [0,1]
#         if number < 2:
#             return result[number]
#         while len(result) < number+1:
#             result.append(2*result[-1])
#         return result[number]

# class Solution:
#     def jumpFloorII(self, number):
#         if number < 0:
#             return -1
#         if number == 0:
#             return 0
#         n = 1
#         number -= 1
#         while number:
#             n *= 2
#             number -= 1
#         return n