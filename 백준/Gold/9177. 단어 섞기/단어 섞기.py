def solution(str1, str2, str3):
    len1, len2, len3 = len(str1), len(str2), len(str3)
    
    if len1 + len2 != len3:
        return False
    
    memo = {}

    def backtracking(i, j, k):
        if k == len3:
            return True
        if (i, j) in memo:
            return memo[(i, j)]
        
        if i < len1 and str1[i] == str3[k]:
            if backtracking(i + 1, j, k + 1):
                memo[(i, j)] = True
                return True
        
        if j < len2 and str2[j] == str3[k]:
            if backtracking(i, j + 1, k + 1):
                memo[(i, j)] = True
                return True
        
        memo[(i, j)] = False
        return False

    return backtracking(0, 0, 0)

n = int(input())

for i in range(n):
    x = input().split()
    if solution(x[0], x[1], x[2]):
        print("Data set %d: yes" % (i+1))
    else:
        print("Data set %d: no" % (i+1))
