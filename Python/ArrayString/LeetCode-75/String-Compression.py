# Problem Statement: https://leetcode.com/problems/string-compression/description/



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

