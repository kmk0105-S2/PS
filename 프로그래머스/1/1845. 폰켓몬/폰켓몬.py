def solution(nums):
    max_value = len(nums)
    count = max_value // 2
    
    nums = set(nums)
    
    if len(nums) >= count:
        return count
    else:
        return len(nums)
    