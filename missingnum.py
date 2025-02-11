def find_missing_number(nums):
    n = len(nums) + 1  # Total numbers should be n
    expected_sum = n * (n + 1) // 2  # Sum of first n natural numbers
    actual_sum = sum(nums)  # Sum of given numbers
    return expected_sum - actual_sum  # Missing number

# Example usage
nums = [1, 2, 4, 5, 6]
missing_number = find_missing_number(nums)
print("Missing number:", missing_number)  # Output: 3
