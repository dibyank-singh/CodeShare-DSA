# Problem Statment: https://leetcode.com/problems/merge-strings-alternately/description

def merge_alternately(word1, word2):
    merged = ""
    # Determine the length of the shorter string
    min_length = min(len(word1), len(word2))

    # Merge alternately until the end of the shorter string
    for i in range(min_length):
        merged += word1[i] + word2[i]

    # Append the remaining characters from the longer string, if any
    merged += word1[min_length:] + word2[min_length:]

    return merged


# Example usage

# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
word1 = "abc"
word2 = "pqr"
result = merge_alternately(word1, word2)
print(result)

# Input: word1 = "ab", word2 = "pqrs"
# Output: "apbqrs"
word1 = "ab"
word2 = "pqrs"
result = merge_alternately(word1, word2)
print(result)


# Input: word1 = "abcd", word2 = "pq"
# Output: "apbqcd"
word1 = "abcd"
word2 = "pq"
result = merge_alternately(word1, word2)
print(result)
