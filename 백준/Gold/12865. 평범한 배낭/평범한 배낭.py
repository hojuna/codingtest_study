def sol():
    N,K=map(int,input().split())
    dp=[[0]*(K+1)  for _ in range(N+1)]
    w=[0]
    v=[0]
    
    for n in range(1,N+1):
        a,b=map(int,input().split())
        w.append(a)
        v.append(b)
    
    for i in range(1,N+1):
        for j in range(1,K+1):
            dp[i][j] = dp[i-1][j];
            if j-w[i]>=0:
                dp[i][j]=max(dp[i-1][j],dp[i-1][j-w[i]]+v[i])
    
    
    
    print(dp[N][K])
sol()