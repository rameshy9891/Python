def is_anagram(word1, word2):
    return sorted(word1) == sorted(word2)

# Test
word1 = "cinema"
word2 = "iceman"
print(is_anagram(word1, word2))  # Output: True
