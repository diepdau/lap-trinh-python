def second_largest_numbers(arr):
    if len(arr) < 2:
        return "Không có số lớn thứ nhì trong mảng"

    max_num = max(arr[0], arr[1])
    second_max = min(arr[0], arr[1])

    for num in arr[2:]:
        if num > max_num:
            second_max = max_num
            max_num = num
        elif num > second_max and num != max_num:
            second_max = num

    return second_max

# Ví dụ sử dụng
my_array = [10, 5, 8, 20, 15]
result = second_largest_numbers(my_array)
print("Số lớn thứ nhì trong mảng là:", result)
