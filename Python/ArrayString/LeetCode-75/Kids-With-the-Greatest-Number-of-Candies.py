# Problem Statement: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/


def kidsWithCandies(candies, extraCandies):
    # Finding Max Candy from candies
    maxCandies = max(candies)
    result = []
    for candy in range(len(candies)):
        # Checking the condition and storing resulting boolean
        result.append(extraCandies + candies[candy] >= maxCandies)

    return result


candies = [2, 3, 5, 1, 3]
extraCandies = 3
print(kidsWithCandies(candies, extraCandies))  # Output: [true,true,true,false,true]


candies = [4, 2, 1, 1, 2]
extraCandies = 1
print(kidsWithCandies(candies, extraCandies))  # Output: [true,false,false,false,false]

candies = [12, 1, 12]
extraCandies = 10
print(kidsWithCandies(candies, extraCandies))  # Output: [true,false,true]
