'''
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
说明：每次只能向下或者向右移动一步。

示例:
输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。

'''

class Solution(object):
    def minPathSum1(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        results = [[0] * n for k in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    results[i][j] = grid[i][j]
                elif i == 0:
                    results[i][j] = results[i][j - 1] + grid[i][j]
                elif j == 0:
                    results[i][j] = results[i - 1][j] + grid[i][j]
                else:
                    results[i][j] = min(results[i - 1][j],
                                        results[i][j - 1]) + grid[i][j]
        return results[m - 1][n - 1]

    def minPathSum2(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    grid[0][j] += grid[0][j - 1]
                    continue
                elif j == 0:
                    grid[i][0] += grid[i - 1][0]
                    continue
                else:
                    grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        return grid[len(grid) - 1][len(grid[0]) - 1]

    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dp = [0] * len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    dp[j] = grid[i][j]
                elif i == 0:
                    dp[j] = dp[j - 1] + grid[i][j]
                elif j == 0:
                    dp[j] = dp[j] + grid[i][j]
                else:
                    dp[j] = min(dp[j], dp[j - 1]) + grid[i][j]
        return dp[len(grid[0]) - 1]


if __name__ == '__main__':
    so = Solution()
    m = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    print(so.minPathSum(m))
