
# Problem Statement: https://leetcode.com/problems/string-compression/description/

"""
    Approach:
    - Use two pointers: `write` for writing the compressed string and `read` for reading through the input characters.
    - Initialize `write` and `read` pointers to 0.
    - While `read` is less than the length of `chars`:
        - Record the current character and initialize a `count` to 0.
        - Use a nested loop to count the occurrences of the current character.
        - Write the character to the `write` position.
        - If the count is greater than 1, write the digits of the count to subsequent positions.
    - Return the `write` pointer which represents the new length after compression.
    """


def compress(chars):
    
    write = 0  # pointer to write in chars
    read = 0   # pointer to read chars

    while read < len(chars):
        char = chars[read]
        count = 0
        
        # Count occurrences of the current character
        while read < len(chars) and chars[read] == char:
            read += 1
            count += 1
        
        # Write the character to the write position
        chars[write] = char
        write += 1
        
        # If count is greater than 1, write the digits of the count
        if count > 1:
            for digit in str(count):
                chars[write] = digit
                write += 1

    return write

# Example usage
chars = ['a', 'a', 'b', 'b', 'c', 'c', 'c']
new_length = compress(chars)
print(f"Compressed List: {chars[:new_length]}, New Length: {new_length}")


chars = ["a"]
new_length = compress(chars)
print(f"Compressed List: {chars[:new_length]}, New Length: {new_length}")

chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
new_length = compress(chars)
print(f"Compressed List: {chars[:new_length]}, New Length: {new_length}")

