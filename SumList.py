def sum_list(list1):
    if len(list1) == 0:
        return "Cannot compute sum for empty list."
    sum = 0
    for i in range(len(list1)):
        sum += list1[i]
    return sum

# Tests
print(sum_list([1, 2, 3, 4, 5]))
print(sum_list([-3, 4, 9, 0, -10]))
print(sum_list([]))
print(sum_list([38, 42]))
print(sum_list([-9]))
