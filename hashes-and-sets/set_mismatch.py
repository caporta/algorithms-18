def find_error(nums):
    ideal_sum = (len(nums) + 1) * len(nums) // 2
    actual_sum = sum(nums)
    diff_sum = sum(set(nums))

    return [actual_sum - diff_sum, ideal_sum - diff_sum]
