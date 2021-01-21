def canSum(targetSum, nums, memo = {}):
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return True
    if targetSum < 0:
        return False
    
    for num in nums:
        currentSum = targetSum - num
        if (canSum(currentSum, nums, memo)) == True:
            memo[targetSum] = True
            return True
    
    memo[targetSum] = False
    return False