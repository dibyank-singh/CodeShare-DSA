# Problem Statement: https://leetcode.com/problems/greatest-common-divisor-of-strings/description/

"""
Approach: 
- The function iterates over possible lengths of the greatest common divisor (GCD) substring, starting from the minimum of the lengths of the input strings down to 1.
- For each length, it checks if both input strings are divisible by that length and if they are equal to multiples of a base substring of that length.
- If a valid GCD substring is found, it returns it. Otherwise, it returns an empty string. 
"""


def gcdOfStrings(str1, str2):
    len1, len2 = len(str1), len(str2)

    def valid(k):
        if len1 % k or len2 % k:
            return False
        n1, n2 = len1 // k, len2 // k
        base = str1[:k]
        return str1 == n1 * base and str2 == n2 * base

    for i in range(min(len1, len2), 0, -1):
        if valid(i):
            return str1[:i]
    return ""


# Example usage:
str1 = "ABCABC"
str2 = "ABC"
print(gcdOfStrings(str1, str2))  # Output: "ABC"

str1 = "ABABAB"
str2 = "ABAB"
print(gcdOfStrings(str1, str2))  # Output: "AB"

str1 = "LEET"
str2 = "CODE"
print(gcdOfStrings(str1, str2))  # Output: ""
