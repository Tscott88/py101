famous_words = "seven years ago..."

# Show two different ways to create a new string with "Four score and " 
# prepended to the front of the string referenced by famous_words.

new_str1 = "Four score and " + famous_words
new_str2 = f"Four score and {famous_words}"

print(new_str1)
print(new_str2)