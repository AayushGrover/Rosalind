def get_rabbits(n, m):
    dp = [1,1,2]

    for i in range(n):
        if i > 2:
            if i-m == 0:
                dp.append(dp[i-1] + dp[i-2] - dp[i-m])
            elif i-m >= 1:
                dp.append(dp[i-1] + dp[i-2] - dp[i-m-1])
            else:
                dp.append(dp[i-1] + dp[i-2])
    return dp[-1]

if __name__ == "__main__":
    n, m = 98, 20
    print(get_rabbits(n, m))