# Original dictionary
my_dict = {'b': 2, 'a': 1, 'c': 3}

# Sort dictionary by keys
sorted_dict = {key: my_dict[key] for key in sorted(my_dict)}

print(sorted_dict)
# Output: {'a': 1, 'b': 2, 'c': 3}
