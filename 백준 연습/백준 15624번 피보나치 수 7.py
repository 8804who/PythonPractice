n = int(input())
dp = [0 for i in range(10000001)]
dp[1] = 1
dp[2] = 1
for i in range(3, n+1):
    dp[i]=(dp[i-1]+dp[i-2])%1000000007
print(dp[n])