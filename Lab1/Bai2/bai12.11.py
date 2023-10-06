def count_occurrences(arr, target):
    count = 0
    for num in arr:
        if num == target:
            count += 1
    return count

# Ví dụ sử dụng
my_array = [2, 3, 2, 5, 6, 2, 8, 2]
target_number = 2
result = count_occurrences(my_array, target_number)
print(f"Số lần xuất hiện của {target_number} trong mảng là:", result)
