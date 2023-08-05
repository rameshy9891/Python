list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

result = [item1 + item2 for item1, item2 in zip(list1, list2)]

print(result)
