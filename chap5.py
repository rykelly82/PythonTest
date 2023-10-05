def find_middle_character (my_string):
    length = len(my_string)
    if length % 2 == 0:
        return None
    return my_string [length // 2]

print(find_middle_character('abdded'))


