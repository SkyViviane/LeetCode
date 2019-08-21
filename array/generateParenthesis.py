"""
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

例如，给出 n = 3，生成结果为：

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

"""


class Solution(object):

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self.dfs(n, n, '', res)
        return res

    def dfs(self, left, right, s, res):
        if left == 0 and right == 0:
            return res.append(s)
        else:
            if left > 0:
                self.dfs(left - 1, right, s + '(', res)
            if right > left:
                self.dfs(left, right - 1, s + ')', res)


so = Solution()
n = 3
print(so.generateParenthesis(n))
