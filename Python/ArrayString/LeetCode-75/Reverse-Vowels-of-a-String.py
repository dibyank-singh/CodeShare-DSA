# Problem Statement: https://leetcode.com/problems/reverse-vowels-of-a-string/description/

"""
Approach: Two Pointer Based
- We start by defining a set of vowels, which includes both lowercase and uppercase vowels.
- We convert the input string s into a list of characters, as strings are immutable in Python and we need to modify them.
- We initialize two pointers, left and right, which point to the beginning and end of the string respectively.
- We iterate through the string with these pointers, moving left pointer towards the right and right pointer towards the left, until they meet or cross each other.
- At each step, we check if the character at the left pointer is a vowel. If it's not a vowel, we increment left pointer to move to the next character. Similarly, we check if the character at the right pointer is a vowel. If it's not a vowel, we decrement right pointer to move to the previous character.
- If both characters at left and right pointers are vowels, we swap them.
- We continue this process until left pointer is less than right pointer.
- Finally, we convert the modified list of characters back into a string and return it.
"""


def reverseVowels(s):
    vowels = set("aeiouAEIOU")
    res = list(s)
    left, right = 0, len(res) - 1

    while left < right:
        while res[left] not in vowels and left < right:
            left += 1
        while res[right] not in vowels and left < right:
            right -= 1

        res[left], res[right] = res[right], res[left]
        left += 1
        right -= 1
    return ''.join(res)


s = "hello"
print(reverseVowels(s))  # Output:  "holle"

s = "leetcode"
print(reverseVowels(s))  # Output:  "leotcede"
