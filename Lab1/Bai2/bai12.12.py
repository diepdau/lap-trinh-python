def find_numbers_with_n_occurrences(arr, n):
    num_occurrences = {}
    result = []

    for num in arr:
        if num in num_occurrences:
            num_occurrences[num] += 1
        else:
            num_occurrences[num] = 1

    for num, occurrences in num_occurrences.items():
        if occurrences == n:
            result.append(num)

    return result

# Ví dụ sử dụng
my_array = [2, 3, 2, 5, 6, 2, 8, 2, 5]
target_occurrences = 3
result = find_numbers_with_n_occurrences(my_array, target_occurrences)
print(f"Các số xuất hiện {target_occurrences} lần trong mảng:", result)
