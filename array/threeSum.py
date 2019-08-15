"""
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]

"""

class Solution(object):
    def threeSum1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        threesum = []
        nums.sort()
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        threesum.append([nums[i], nums[j], nums[k]])
        threesum = list(set([tuple(t) for t in threesum]))
        threesum = [list(v) for v in threesum]
        return threesum

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        threesum = []
        nums.sort()

        for k in range(len(nums) - 2):
            i = k + 1
            j = len(nums) - 1
            if nums[k] > 0:
                break
            if k > 0 and nums[k] == nums[k - 1]:
                continue
            while i < j:
                s = nums[k] + nums[i] + nums[j]
                if s < 0:
                    i += 1
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                elif s > 0:
                    j -= 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
                else:
                    threesum.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
        return threesum


so = Solution()
nums = []
print(so.threeSum(nums))
