import numpy as np

def triangle_shortest_path(n, tri):
    dp = [[0 for col in range(n)] for row in range(n)]
    dp[0][0] = tri[0][0]
    for i in range(1, n):
        dp[i][0] = dp[i - 1][0] + tri[i][0]
        for j in range(1, i):
            dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j]) + tri[i][j]
        dp[i][i] = dp[i - 1][i - 1] + tri[i][i]
    temp = dp[n - 1][0]
    for k in range(1, n):
        temp = min(temp, dp[n - 1][k])
    return temp
        
    
if __name__=='__main__':
    n = int(input().strip())
    tri = [[0] * n] * n
    for i in range(n):
         tri[i] = list(map(int, input().split())) 
#     n = 4
#     tri = [[2, 0, 0, 0], [3, 4, 0, 0], [6, 5, 7, 0], [4, 1, 8, 3]]
    print(triangle_shortest_path(n, tri))
