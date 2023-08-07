def add_name_age(dictionary, name, age):
    dictionary[name] = age

def update_age(dictionary, name, new_age):
    if name in dictionary:
        dictionary[name] = new_age

def delete_name(dictionary, name):
    if name in dictionary:
        del dictionary[name]

# Test
data = {}
add_name_age(data, "John", 25)
print(data)  # Output: {'John': 25}

update_age(data, "John", 26)
print(data)  # Output: {'John': 26}

delete_name(data, "John")
print(data)  # Output: {}
