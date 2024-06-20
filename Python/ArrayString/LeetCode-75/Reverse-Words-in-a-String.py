# Problem Statement: https://leetcode.com/problems/reverse-words-in-a-string/description/

"""
Approach:
- Split the string into words using the split() method.
- Reverse the list of words using the reverse() method.
- Join the reversed words into a string using the join() method with a single space separator.
"""


def reverseWords(s):
    words = s.split()
    words.reverse()
    return " ".join(words)


# Example usage:
print(reverseWords("the sky is blue"))  # Output: "blue is sky the"
print(reverseWords("  hello world  "))  # Output: "world hello"
print(reverseWords("a good   example"))  # Output: "example good a"
