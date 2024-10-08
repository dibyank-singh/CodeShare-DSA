#Leetcode   QA-42. Trapping Rain Water

class Solution:
    def trap(self, height):
        if not height or len(height) < 3:
            return 0

        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        water_trapped = 0

        # Two pointers approach
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water_trapped += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water_trapped += right_max - height[right]
                right -= 1

        return water_trapped




# Example Walkthrough:

# Let’s say we have the input: height = [0,1,0,2,1,0,1,3,2,1,2,1].

# Initial States: left = 0, right = 11, left_max = 0, right_max = 0, water_trapped = 0.
# As the loop runs, it checks and calculates water trapped between the bars based on the heights, eventually leading to a final count of 6 for this example.
# Time Complexity:
# The time complexity of this solution is 
# 𝑂
# (
# 𝑛
# )
# O(n), where 
# 𝑛
# n is the number of elements in the height list. This is because each element is processed once by the two-pointer approach.
# Space Complexity:
# The space complexity is 
# 𝑂
# (
# 1
# )
# O(1), as we are using a fixed amount of extra space regardless of the input size.