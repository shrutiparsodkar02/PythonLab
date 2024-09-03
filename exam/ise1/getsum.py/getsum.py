def get_sum(input_list):
    total = 0
    for element in input_list:
        elem_type = type(element)
        if elem_type == int or elem_type == float or elem_type == complex:
            total += element
        elif elem_type == list or elem_type == tuple:
            total += get_sum(element)
    return total

# Sample usages
print(get_sum([1, 2.4, 3, '4']))           # Output: 6.4
print(get_sum(["SGGS", [3, '3', [1]], 2])) # Output: 6
print(get_sum(["1", (2, 3), 1]))           # Output: 6
