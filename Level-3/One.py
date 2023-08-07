def print_names_and_ages(data):
    for name, age in data:
        print(f"{name} is {age} years old.")

# Test
data = [("John", 25), ("Jane", 30)]
print_names_and_ages(data)
