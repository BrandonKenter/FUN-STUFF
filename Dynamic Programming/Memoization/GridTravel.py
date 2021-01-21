def gridTraveler(m, n, memo = {}):
    key = str(m) + "," + str(n)

    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    if key in memo:
        return memo[key]

    memo[key] = gridTraveler(m - 1, n, memo) + gridTraveler(m, n - 1, memo)
    
    return memo[key]