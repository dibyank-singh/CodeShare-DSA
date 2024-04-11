# Problem Statement: https://leetcode.com/problems/can-place-flowers/description/

"""
Approach:
- Iterate through each plot in the flowerbed.
- Check if the current plot and its adjacent plots (if they exist) are all empty (i.e., equal to 0).
- Handle boundary cases separately to ensure proper checking.
- If the conditions are met, plant a flower in the current plot and increment the count.
- Finally, return true if the count of planted flowers is greater than or equal to the required number 
"""


def canPlaceFlowers(flowerbed, n):
    count = 0
    for i in range(len(flowerbed)):
        if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
            flowerbed[i] = 1
            count += 1

    return count >= n



flowerbed = [1, 0, 0, 0, 1]
n = 1
print(canPlaceFlowers(flowerbed, n))  # Output: true

flowerbed = [1, 0, 0, 0, 1]
n = 2
print(canPlaceFlowers(flowerbed, n))  # Output: false

flowerbed = [1, 0, 0, 0, 0, 1]
n = 2
print(canPlaceFlowers(flowerbed, n))  # Output: false
