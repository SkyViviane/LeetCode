arr = [[1,0,1,0,0],[1,0,1,1,1],[1,1,1,1,1],[1,0,0,1,0],[1,0,0,0,0],[1,0,0,0,0],[1,0,0,0,0],[1,0,0,0,0]]

def area(arr):
    maxarea = 0
    n = len(arr)
    m = len(arr[0])
    dp = [[0] * m  for row in range(n)]
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0: continue
            width = dp[i][j] = dp[i][j - 1] + 1 if j else 1
            for k in range(i, -1, -1):   
                width = min(width, dp[k][j])
                maxarea = max(maxarea, width * (i - k + 1))
    return maxarea
area(arr)
    
