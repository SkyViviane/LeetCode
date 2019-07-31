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
