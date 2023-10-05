def get_middle_character(input):
    length = len(input)

    # Return None for strings with an even length
    if length % 2 == 0:
        return None

   # else: length > 0

    return input[length // 2]

# For example this will print 'c'
print(get_middle_character('abcde'))
