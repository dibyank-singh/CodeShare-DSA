# Problem Statement: https://leetcode.com/problems/increasing-triplet-subsequence/description/

"""
Approach:
- The goal is to find three numbers in the array that form an increasing triplet.
- We will use two variables, `first` and `second`, to keep track of the smallest and the second smallest numbers found so far.
- As we iterate through the array:
  - We update `first` if the current number is smaller than `first`.
  - We update `second` if the current number is greater than `first` but smaller than `second`.
  - If we find a number greater than both `first` and `second`, it means we have found an increasing triplet.
- If no such triplet is found by the end of the array, we return False.
- This approach works in O(n) time complexity with O(1) space complexity, making it efficient for large input sizes.
"""

def increasingTriplet(nums):
    if len(nums) < 3:
        return False

    first = float('inf')
    second = float('inf')

    for num in nums:
        if num <= first:
            first = num  # update first if num is smaller
        elif num <= second:
            second = num  # update second if num is smaller
        else:
            # If we find a number greater than both first and second, we have found the triplet
            return True

    return False

# Example usage
print(increasingTriplet([1, 2, 3, 4, 5]))  # Output: True

print(increasingTriplet([5, 4, 3, 2, 1]))  # Output: False

print(increasingTriplet([2, 1, 5, 0, 4, 6]))  # Output: True
