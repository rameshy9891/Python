str1 = "PyNaTive"
lowercase_chars = [char for char in str1 if char.islower()]
uppercase_chars = [char for char in str1 if char.isupper()]
result = ''.join(lowercase_chars + uppercase_chars)

print(result)
