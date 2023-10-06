#Đổi chỗ 2 phần tử của danh sách, đầu vào là 2 vị trí cần đổi chỗ
def swap_elements(arr, pos1, pos2):
    if pos1 < 0 or pos1 >= len(arr) or pos2 < 0 or pos2 >= len(arr):
        print("Invalid positions")
        return
    
    arr[pos1], arr[pos2] = arr[pos2], arr[pos1]

# Ví dụ sử dụng
my_array = [1, 2, 3, 4, 5]
print("Mảng trước khi đổi chỗ:", my_array)

position1 = 1  # Vị trí cần đổi chỗ
position2 = 3  # Vị trí khác cần đổi chỗ

swap_elements(my_array, position1, position2)

print("Mảng sau khi đổi chỗ:", my_array)
