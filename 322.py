def coinChangeDP(coins, rem, count: List[int]):
    dp = [0] + [float('inf') for _ in range(s)]
    for v in c:
        for i in range(v,s+1):
            dp[i] = min(dp[i], dp[i-v]+1)
    if dp[s] == float('inf'): return -1
    return dp[s]
