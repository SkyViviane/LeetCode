def lcs(a, b):
    n = min(len(a), len(b))
    dp = [[0 for col in range(n)] for row in range(n)]
    for i in range(n):
        for j in range(n):
            if a[i] == b[j]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[n - 1][n - 1]

if __name__=='__main__':
    a = [1,3,4,5,6,7,7,8]
    b = [3,5,7,4,8,6,7,8,2]
    print(lcs(a, b))
