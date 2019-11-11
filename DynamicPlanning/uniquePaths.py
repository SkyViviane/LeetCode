'''
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
问总共有多少条不同的路径？

例如，上图是一个7 x 3 的网格。有多少可能的路径？
说明：m 和 n 的值均不超过 100。

示例 1:
输入: m = 3, n = 2
输出: 3
解释:
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向右 -> 向下
2. 向右 -> 向下 -> 向右
3. 向下 -> 向右 -> 向右

示例 2:
输入: m = 7, n = 3
输出: 28

'''

class Solution(object):
    def uniquePaths1(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 1 and n == 1:
            return 1
        return self.walk(1, 1, m, n)

    def walk(self, x, y, m, n):
        down = 0
        right = 0
        if x >= m or y >= n:
            return 1
        down = self.walk(x + 1, y, m, n)
        right = self.walk(x, y + 1, m, n)
        return down + right

    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        results = [0] * n
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    results[j] = 1
                else:
                    results[j] += results[j - 1]
        return results[n - 1]


if __name__ == '__main__':
    so = Solution()
    m = 23
    n = 12
    print(so.uniquePaths(m, n))
