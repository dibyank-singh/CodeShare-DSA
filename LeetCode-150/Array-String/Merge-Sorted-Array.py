
# // LeetCode Series- QA(1)
# 88. Merge Sorted Array

# QA for reference

# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.



# // Solution


def merge_sorted_array(arr1, size1, arr2, size2):
    i = size1 - 1
    j = size2 - 1
    k = size1 + size2 - 1

    while i >= 0 and j >= 0:
        if arr1[i] > arr2[j]:
            arr1[k] = arr1[i]
            i -= 1
        else:
            arr1[k] = arr2[j]
            j -= 1
        k -= 1

    while j >= 0:
        arr1[k] = arr2[j]
        j -= 1
        k -= 1

# Example
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

merge_sorted_array(nums1, m, nums2, n)
print(nums1)


# // Time complexity
# The time complexity of this solution is O(m + n), where m and n are the sizes of the two input arrays.


# // A brief explanation of the approach 

# Initialization: We initialize three pointers: i pointing to the last element of the first array (arr1), j pointing to the last element of the second array (arr2), and k pointing to the last element of the merged array.

# Merge: We iterate through the arrays starting from their ends. At each iteration, we compare the elements at arr1[i] and arr2[j]. The larger element is placed at arr1[k], and the corresponding pointer (i or j) is decremented. We move k to the previous position to store the next element.

# Remaining elements: After the above loop, if there are still elements left in arr2, we copy them to the remaining positions in arr1. This step ensures that all elements from both arrays are merged properly.