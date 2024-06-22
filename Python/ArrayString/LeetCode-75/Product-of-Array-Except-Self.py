# Problem Statement: https://leetcode.com/problems/product-of-array-except-self/description/

# SECTION 1 : Brute Force
"""
Brute Force Approach:
- Iterate through each element of nums.
- For each element at index i, initialize a variable product to 1.
- Iterate through the array again to multiply all elements except nums[i] to product.
- Store the result in the answer array.
"""


def productExceptSelf(nums):
    n = len(nums)
    answer = [0] * n

    for i in range(n):
        product = 1
        for j in range(n):
            if j != i:
                product *= nums[j]
        answer[i] = product

    return answer


# Example usage:
nums1 = [1, 2, 3, 4]
nums2 = [-1, 1, 0, -3, 3]

print(productExceptSelf(nums1))  # Output: [24, 12, 8, 6]
print(productExceptSelf(nums2))  # Output: [0, 0, 9, 0, 0]


# SECTION 2 : Prefix Multiplication

"""
Prefix Multiplication Approach:
The prefix multiplication approach calculates the products of elements to the left and right of each element using two passes through the array (prefix_prod for left products and suffix_prod for right products):
"""


def productExceptSelf(nums):
    n = len(nums)
    res = [1] * n

    prefix_prod = 1
    for i in range(n):
        res[i] *= prefix_prod
        prefix_prod *= nums[i]

    suffix_prod = 1
    for j in range(n - 1, -1, -1):
        res[j] *= suffix_prod
        suffix_prod *= nums[j]

    return res


# Example usage:
nums1 = [1, 2, 3, 4]
nums2 = [-1, 1, 0, -3, 3]

print(productExceptSelf(nums1))  # Output: [24, 12, 8, 6]
print(productExceptSelf(nums2))  # Output: [0, 0, 9, 0, 0]
