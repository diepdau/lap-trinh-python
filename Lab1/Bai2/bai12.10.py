def sum_of_digits(num):
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    return total

def sum_of_digits_in_array(arr):
    total_sum = 0
    for num in arr:
        total_sum += sum_of_digits(num)
    return total_sum

# Ví dụ sử dụng
my_array = [123, 45, 67, 89]
result = sum_of_digits_in_array(my_array)
print("Tổng các chữ số trong mảng là:", result)
