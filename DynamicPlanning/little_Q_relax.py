"""
公司给小Q放了n天的假，他有个奇怪的习惯：不会连续两天工作或段炼，只有当公司开业，小Q才能去工作，只有当健身房营业时，小O才能去健身，小Q一天只能干一件事。
给出假期中公司、健身房的营业情兄，求小Q最少需要体息几天？

输入描述：
第一行一个数表示放假天数n
第二行n个数字，数字为0或者1,第i个数表示公司在第1天是否营业
第三行n个数字，数字为0或者1,第i个数表示健身房在第i天是否营业
（1为营业0为不营业)

输入
4
1 1 0 0
0 1 1 0

输出
2

说明：小Q可以在第一天工作，第二或者第三健身，最少休息两天
"""

#未完，通过率10%
def relax(n, work, fitness):
    w = [0] * n
    f = [0] * n
    wf = [0] * n
    count = 0
    i = 0
    while 0 <= i < n:
        if work[i] == 1 and fitness[i] == 0:
            w[i] = 1
            i += 2
        elif work[i] == 1:
            w[i] = 1
            i += 2
        else:
            i += 1
    print("w:", w)
    
    j = 0
    while 0 <= j < n:
        if work[j] == 0 and fitness[j] == 1:
            w[j] = 1
            j += 2
        if fitness[j] == 1:
            f[j] = 1
            j += 2
        else:
            j += 1
    print("f:", f)
            
    for k in range(n):
        wf[k] = w[k] + f[k]
        if wf[k] == 0:
            count += 1
    return count
            
if __name__=='__main__':
#     n = int(input().strip())
#     work = list(map(int, input().strip().split()))
#     fitness = list(map(int, input().strip().split()))
    n = 10
    work = [0, 1, 0, 0, 1, 1, 1, 0, 1, 1]
    fitness = [1, 1, 1, 1, 0, 0, 1, 1, 1, 1]
    print(relax(n, work, fitness))                    
 

#通过率100%
def min_relax(n, work, fitness):
    
    # dp[0][i]表示第i天休息的最少的休息天数，dp[1][i]表示第i天工作最少的休息天数，dp[2][i]表示第i天健身最少的休息天数
    dp = [[0 for col in range(n)] for row in range(3)]
    dp[0][0] = 1
    if work[0] == 1: dp[1][0] = 0
    if fitness[0] == 1: dp[2][0] = 0
    for i in range(1, n):
        if work[i] == 1:
            if fitness[i - 1] == 1:
                dp[1][i] = min(dp[0][i - 1], dp[2][i - 1])
            else:
                dp[1][i] = dp[0][i - 1]
        else:
            dp[1][i] = n
        if fitness[i] == 1:
            if work[i - 1] == 1:
                dp[2][i] = min(dp[0][i - 1], dp[1][i - 1])
            else:
                dp[2][i] = dp[0][i - 1]
        else:
            dp[2][i] = n
        
        dp[0][i] = min(dp[0][i - 1], dp[1][i - 1], dp[2][i - 1]) + 1
    return min(dp[0][n - 1], dp[1][n - 1], dp[2][n - 1])

if __name__=='__main__':
#     n = 4
#     work = [1, 1, 0, 0]
#     fitness = [0, 1, 1, 0]
    n = int(input())
    work = list(map(int, input().split()))
    fitness = list(map(int, input().split()))
    print(min_relax(n, work, fitness))
