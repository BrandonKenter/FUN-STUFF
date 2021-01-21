def howSum(targetSum, nums, memo = {}):
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None

    for num in nums:
        currentSum = targetSum - num
        result = howSum(currentSum, nums, memo)
        if result is not None:
            result.append(num)
            memo[targetSum] = result
            return result

    memo[targetSum] = None
    return None