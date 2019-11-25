'''
给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。

示例 1:

输入: "(()"
输出: 2
解释: 最长有效括号子串为 "()"
示例 2:

输入: ")()())"
输出: 4
解释: 最长有效括号子串为 "()()"

'''


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [0] * len(s)
        maxans = 0
        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i - 1] == '(':
                    dp[i] = dp[i - 2] + 2
                else:
                    if i - dp[i - 1] >= 1 and s[i - dp[i - 1] - 1] == '(':
                        dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2
            maxans = max(maxans, dp[i])
        print(dp[-1])
        return maxans


if __name__ == '__main__':
    so = Solution()
    s = "(()))())("
    print(so.longestValidParentheses(s))
