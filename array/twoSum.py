'''
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

'''


class Solution:
    def twoSum(self, nums, target: int):
        if len(nums) <= 1 or nums is None:
            return -1
        for i in range(len(nums)):
            if target - nums[i] in nums[i + 1:]:
                return [i, nums.index(target - nums[i], i + 1)]


if __name__ == '__main__':
    so = Solution()
    arr = [5, 1, 5, 5, 2, 5, 4]
    k = 10
    print(so.twoSum(arr, k))

    
'''
num = [1,2,3,4,5,6,7,8,9]   #nums 为一个有序数组
给定k
求nums中两数之和为k的数的下标

如 k =10
返回结果为 [[0,8],[1,7],[2,6],[3,5]]
ps: 小提示   nums数组可能存在两数相等的情况 
    如：nums = [1,2,3,3,4,5,6,7,7,8,9,9]
'''
   
def twoNums(nums, k):
    lens = len(nums)
    temp = []
    res = []
    for i in range(lens):
        one = nums[i]
        two = k - nums[i]
        for j in range(i + 1, lens):
            if nums[j] == two:
                temp.append(i)
                temp.append(j)
                res.append(temp)
                temp = []
    return res
                  
nums = [1,2,3,3,4,5,6,7,7,8,9,9]
k = 10
print(twoNums(nums, k))

#利用了有序数组的特性
def twoNums(nums, k):
    lens = len(nums)
    res = []
    temp = []
    for l in range(lens):
        r = lens - 1
        while l < r:
            m = k - nums[l]
            if m == nums[r]:
                temp.append(l)
                temp.append(r)
                res.append(temp)
                temp = []
                if nums[r] == nums[r - 1]:
                    r -= 1
                else:
                    break
            elif m > nums[r]:
                l += 1
            else:
                r -= 1
        
    return res
              
nums = [1,2,3,3,4,5,6,7,7,8,9,9]
k = 10
print(twoNums(nums, k))
