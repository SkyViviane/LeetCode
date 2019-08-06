'''
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21
注意:

假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^31 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。

'''


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        n = x if x > 0 else -x
        ans = 0
        while n != 0:
            a = n % 10
            if ans > (2 ** 31 - 1) // 10 or (ans == (2 ** 31 - 1) // 10 and a > 7):
                return 0
            if ans < -2 ** 31 // 10 or (ans == -2 ** 31 // 10 and a < -8):
                return 0
            ans = ans * 10 + a
            n //= 10
        return ans if x > 0 else -ans


so = Solution()
x = -123
print(so.reverse(x))
