def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

# Test
n = 16
print(is_power_of_two(n))  # Output: True
