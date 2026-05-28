def short_long_short(str1, str2):
    if len(str1) > len(str2):
        result = str2 + str1 + str2
    else:
        result = str1 + str2 + str1

    return result

# These examples should all print True
print(short_long_short('abc', 'defgh') == "abcdefghabc")
print(short_long_short('abcde', 'fgh') == "fghabcdefgh")
print(short_long_short('', 'xyz') == "xyz")