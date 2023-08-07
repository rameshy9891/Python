def divide_numbers(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Cannot divide by zero."

# Test
numerator = 5
denominator = 0
print(divide_numbers(numerator, denominator))  # Output: "Cannot divide by zero."
