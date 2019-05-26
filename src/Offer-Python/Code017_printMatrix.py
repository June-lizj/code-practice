# 输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字
# 例如，如果输入如下4 X 4矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
# 则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        result = []
        while matrix:
            result += matrix.pop(0)
            if matrix and matrix[0]:
                for row in matrix:
                    result.append(row.pop())
            if matrix and matrix[0]:
                result += matrix.pop()[::-1]
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    result.append(row.pop(0))
        return result


t0 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
t1 = [[1],[2],[3]]
t2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
s = Solution()
print(s.printMatrix(t2))

# 1.只有一个元素时，取出后继续pop报错
# 2.多个列表，每个列表只有一个元素时，pop取出后[]算作一个元素
# 3.列表逆序方法[::-1]
# 4.考虑完整的测试用例