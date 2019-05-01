# 给定一个double类型的浮点数base和int类型的整数exponent。
# 求base的exponent次方。

class Solution:
    def Power(self, base, exponent):
        if base == 0.0 and exponent < 0:
            return None
        return base**exponent

s = Solution()
bases = [1,2,0,-1,-2]
exponents = [1,2,0,-1,-2]
for base in bases:
    for exponent in exponents:
        print('base:',base,'exponent:',exponent,'power:',s.Power(base,exponent))