"""
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.

与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).

"""

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        nums.sort()
        sum = nums[0] + nums[1] + nums[2]
        for k in range(len(nums) - 2):
            i = k + 1
            j = len(nums) - 1
            while i < j:
                temp = nums[k] + nums[i] + nums[j]
                if abs(temp - target) < abs(sum - target):
                    sum = temp
                if temp > target:
                    j -= 1
                elif temp < target:
                    i += 1
                else:
                    return sum
        return sum

so = Solution()
nums = [1, 2, 4, 8, 16, 32, 64, 128]
m = 82
print(so.threeSumClosest(nums, m))
