def KtraBinhPhuong(number):
    sqrt_num = int(number ** 0.5)
    return sqrt_num * sqrt_num == number

def laFibonacci(number):
    if number < 0:
        return False

    return KtraBinhPhuong(5 * number * number + 4) or KtraBinhPhuong(5 * number * number - 4)

n = int(input("Nhập số nguyên n: "))
while n<0:
    print("Nhap khong hop le! Vui long nhap lai: ")
    n = int(input("Nhập số nguyên n: "))

if laFibonacci(n):
    print(f"{n} là số Fibonacci.")
else:
    print(f"{n} không là số Fibonacci.")


# def is_perfect_square(number):

# Đây là một hàm con (helper function) được sử dụng để kiểm tra xem một số có phải là bình phương hoàn hảo hay không.
# sqrt_num = int(number ** 0.5)

# Hàm này tính căn bậc hai của số được truyền vào bằng cách sử dụng phép toán ** (mũ).
# number ** 0.5 là cách tính căn bậc hai của number.
# int(...) được sử dụng để làm tròn giá trị kết quả của căn bậc hai xuống dưới dạng số nguyên.
# return sqrt_num * sqrt_num == number

# Hàm này trả về True nếu number là một bình phương hoàn hảo (căn bậc hai của number là một số nguyên và bình phương của số nguyên đó bằng number), ngược lại trả về False.
# def is_fibonacci(number):

# Đây là hàm chính để kiểm tra xem một số có phải là số Fibonacci hay không.
# if number < 0: và return False

# Trước hết, hàm kiểm tra xem số có âm không phải là số Fibonacci. Vì dãy Fibonacci chỉ chứa các số không âm.
# return is_perfect_square(5 * number * number + 4) or is_perfect_square(5 * number * number - 4)

# Hàm này kiểm tra xem số number có phải là số Fibonacci bằng cách kiểm tra xem 5 * number * number + 4 hoặc 5 * number * number - 4 có là bình phương hoàn hảo hay không.
# Quan sát rằng nếu một số là số Fibonacci, thì một trong hai biểu thức trên phải là bình phương hoàn hảo.
# Cuối cùng, sau khi xác định xem số có phải là số Fibonacci hay không, chương trình sẽ in ra thông báo tương ứng.

# Chương trình này sử dụng tính chất liên quan đến dãy số Fibonacci và tính chất của bình phương hoàn hảo để kiểm tra xem một số có thuộc dãy Fibonacci hay không.