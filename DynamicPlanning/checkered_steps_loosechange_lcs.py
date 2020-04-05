def go_square(tag, n, m):
    dp = [[0 for col in range(m)] for row in range(n)]
    dp[0][0] = tag[0][0]
    for i in range(1, n):
        dp[i][0] = dp[i - 1][0] + tag[i][0]
    for j in range(1, m):
        dp[0][j] = dp[0][j - 1] + tag[0][j]
        
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + tag[i][j]
    return dp[n - 1][m - 1]
    
if __name__=='__main__':
    #tag = [[random.randint(1, 10) for col in range(4)] for row in range(3)]
    tag = [[1, 2, 3], [1, 1, 1]]
    n = 2
    m = 3
    print(go_square(tag, n, m))
    
    
def go_square(tag, n, m):
    dp = [[0 for col in range(m)] for row in range(n)]
    dp[0][0] = tag[0][0]
    for i in range(1, n):
        dp[i][0] = dp[i - 1][0] + tag[i][0]
    for j in range(1, m):
        dp[0][j] = dp[0][j - 1] + tag[0][j]
        
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + tag[i][j]
    return dp[n - 1][m - 1]
    
if __name__=='__main__':
    #tag = [[random.randint(1, 10) for col in range(4)] for row in range(3)]
    tag = [[1, 2, 3], [1, 1, 1]]
    n = 2
    m = 3
    print(go_square(tag, n, m))
