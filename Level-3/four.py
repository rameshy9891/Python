def is_palindrome(word):
    return word == word[::-1]

# Test
word = "madam"
if is_palindrome(word):
    print(f"The word {word} is a palindrome.")
else:
    print(f"The word {word} is not a palindrome.")
