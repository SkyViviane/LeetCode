class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                m = j + 1
                n = len(nums) - 1
                while m < n:
                    temp = nums[i] + nums[j] + nums[m] + nums[n]
                    if temp < target:
                        m += 1
                    elif temp > target:
                        n -= 1
                    else:
                        res.append([nums[i], nums[j], nums[m], nums[n]])
                        m += 1
                        n -= 1

        res = list(set([tuple(num) for num in res]))
        res = [list(num) for num in res]
        return res


so = Solution()
nums = [1, -2, -5, -4, -3, 3, 3, 5]
target = -11
print(so.fourSum(nums, target))
