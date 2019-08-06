'''
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 。
'''


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        s = ""
        j = 0
        while j < len(strs[0]):
            for i in range(len(strs)):
                try:
                    a = strs[i][j]
                except:
                    a = None
                if a is None or not a.__eq__(strs[0][j]):
                    return s
            s += strs[0][j]
            j += 1

        return s


so = Solution()
strs = ["tt", "t"]
print(so.longestCommonPrefix(strs))
