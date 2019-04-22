# 把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
# 输入一个非减排序的数组的一个旋转，输出旋转数组的最小元素。
# 例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
# NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。

class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if not rotateArray:
            return 0
        elif len(rotateArray) == 1:
            return rotateArray[0]
        else:
            left = 0
            right = len(rotateArray) - 1
            while left < right:
                mid = int((left + right)/2)
                if rotateArray[mid] > rotateArray[right]:
                    left = mid + 1
                elif rotateArray[mid] == rotateArray[right]:
                    right = right - 1
                else:
                    # 因为mid总是取偏小的值,所以输入[4,6]时left=0,right=1,mid = 0
                    # 若right = mid - 1,right = -1,偏离本意
                    # 这个题是选最小的值,用left所以无影响,但如果取最大的值,就会出bug
                    right = mid
            return rotateArray[left]

# 1.非空检查,单个元素检查
# 2.小数取整问题,int(),round(),math包的ceil()
# 3.因为int()取整一直偏小,所以left = mid + 1,而right = mid
# 4.可能会有重复元素,所以mid == right时,要right = right -1逐个递减

# 0.遍历整个数组(纯傻子)
# 1.min()函数(不能用)
# 2.相邻元素比较(有点傻)
# 3.先排序,再返回(纯傻子)
# 4.二分法
