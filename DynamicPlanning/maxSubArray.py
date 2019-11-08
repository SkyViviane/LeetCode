'''
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

'''


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        ans = nums[0]
        for i in range(0, len(nums)):
            if sum > 0:
                sum += nums[i]
            if sum <= 0:
                sum = nums[i]
            ans = max(ans, sum)
            print(ans)
        return ans


if __name__ == '__main__':
    so = Solution()
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(so.maxSubArray(nums))
