def total_value(N, K):
    # dp를 적용할 2차원 배열리스트 생성
    dp = [[0] * (K + 1) for _ in range(N+1)]
    
    # 최댓값 갱신
    for i in range(1, N+1):
        weight, value = map(int, input().split())
        for j in range(1, K+1):
            if j < weight:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight] + value)

    print(dp[N][K])

N, K = map(int, input().split())
total_value(N, K)