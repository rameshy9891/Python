import itertools

def string_permutations(s):
    return ["".join(perm) for perm in itertools.permutations(s)]

# Test
s = "abc"
print(string_permutations(s))  # Output: ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
