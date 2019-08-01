'''
给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格

设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:
你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）
卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)   
示例:
输入: [1,2,3,0,2]
输出: 3 
解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]
'''


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n < 2:
            return 0
        if n == 2:
            return prices[1] - prices[0] if prices[1] > prices[0] else 0

        dp1 = [0] * n
        dp2 = [0] * n
        dp2[0] = - prices[0]
        for i in range(1, n):
            dp1[i] = max(dp1[i - 1], dp2[i - 1] + prices[i])
            if i >= 2:
                dp2[i] = max(dp2[i - 1], dp1[i - 2] - prices[i])
            else:
                dp2[i] = max(dp2[i - 1], - prices[i])
        return dp1[n - 1]


if __name__ == '__main__':
    so = Solution()
    prices = [1, 2, 4]
    print(so.maxProfit(prices))
