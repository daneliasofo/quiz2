def cube_list(numbers):
    result = []
    for num in numbers:
        result.append(num ** 3)
    return result


nums = [1, 2, 3, 4]
print(cube_list(nums))
