def most_common_numbers(arr):
    num_occurrences = {}
    max_occurrences = 0

    for num in arr:
        if num in num_occurrences:
            num_occurrences[num] += 1
        else:
            num_occurrences[num] = 1
        max_occurrences = max(max_occurrences, num_occurrences[num])

    most_common_nums = []
    for num, occurrences in num_occurrences.items():
        if occurrences == max_occurrences:
            most_common_nums.append(num)

    return most_common_nums

# Ví dụ sử dụng
my_array = [2, 3, 2, 5, 6, 2, 8, 5, 5]
result = most_common_numbers(my_array)
print("Các số xuất hiện nhiều lần nhất trong mảng:", result)
