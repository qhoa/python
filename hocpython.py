# Bài 1 Codelearn in màn hình hello
print("Hello, World!")

# Bài 2 Codelearn in màn hình chuỗi
print("Welcome to Codelearn.io!")

# Bài 3 Codelearn hiển thị kết quả của phép tổng số học
print(3273 + 2282)

# Bài 4 Codelearn hiển thị kết quả của phép công trừ nhân chia
print("2468 + 1234 =", 2468 + 1234)
print("2468 - 1234 =", 2468 - 1234)
print("2468 * 1234 =", 2468 * 1234)
print("2468 / 1234 =", 2468 / 1234)

# Bài 5 Codelearn hiển thị kết quả bao gồm cả chuỗi và phép tính
print("Area =", 6.4 * 7.8)
print("Perimeter =", (6.4 + 7.8) * 2)

# Bài 6 Codelearn hướng dẫn comment # dòng và ''' khối

# Bài 7 Code learn định nghĩa các loại kiểu dữ liệu int float string boolean
## Initialization an integer variable name num_integer
num_integer = 1000
## Initialization a float variable name num_float
num_float = 3.125
## Initialization a string variable name string_var
string_var = 'Codelearn.io'
## Initialization a boolean variable name boolean_var
boolean_var = True

##Print value of each variable
print(num_integer)
print(num_float)
print(string_var)
print(boolean_var)

# Bài 9 Codelearn thục hành thêm kiến thức (8)
num_integer = 5000
num_float = 1.2345
string_var = "Codelearn.io"
boolean_var = False

print(num_integer)
print(num_float)
print(string_var)
print(boolean_var)

# Bài 10 Codelearn hiễn thị kết quả kết hợp giữa chuỗi , biến
name = "Codelearn"
date_of_birth = 2019
print("Name: " + name)
print("Date of birth: " + str(date_of_birth))

# Bài 11 Codelearn hiễn thị kết quả kết hợp giữa chuỗi , biến
a = 438
b = 636
cong = a + b
tru = a - b
nhan = a * b
chia = a /b
print("a + b = " + str(cong))
print("a - b = " + str(tru))
print("a * b = " + str(nhan))
print("a / b = " + str(chia))

# Bài 12 Codelearn hiễn thị kết quả kết hợp giữa chuỗi , biến
length = 7.8
width = 3.5
dientich = length * width
chuvi = (length + width)*2
print("Area: " + str(dientich))
print("Perimeter: " + str(chuvi))

# Bài 13 Codelearn nhập thông tin
name = input()
print("Hello " + name)

# Bài 14 Codelearn nhập thông tin và tính toán
name = input()
age = int(input())
print("In 15 years, age of " + name + " will be " + str(15 + age))

# Bài 15 Codelearn nhập thông tin và tính toán, in ra giá trị phần dư của phép chia a / b

a = int(input())
b = int(input())
print("a % b =", str(a % b))

# Bài 31 Codelearn kiến thức vòng lặp while.
'''
n = int(input())
i = 1
while i < n:
    print(i)
    i += 1
'''
## Bài tập (1) tính phép cộng tổng sau mỗi vòng lặp
n = int(input())
i = 1
tong = 0
while i < n:
    tong += i
    i += 1
    print(tong)
# Bài 32 Codelearn kiến thức vòng lặp while.
## Bài tập (2) tính tổng các số lẻ từ a đến b
a = int(input())
b = int(input())
tong = 0

while a <= b:
    if a % 2 !=0:
        tong += a
    a += 1
print(tong)

# Bài 33 Codelearn kiến thức vòng lặp for.
'''
#Break cho phép dừng, thoát vòng lặp khi match điều kiện không thiển thị thêm dữ liệu
for i in range(1, 11):
    if i == 6:
        break
    print(i)
#Continue cho phép tiếp tục vòng lặp khi match điều kiện và bỏ qua giá trị hiển thị
for i in range(1, 20):
    if i % 2 == 0:
        continue
    print(i)
'''
## Bài tập (1) in ra toàn bộ ký tự và bỏ qua 'y' trong trong chuỗi nếu có
s = input()
for c in s:
    if c == 'y':
        continue
        print("Current character:", c)

# Bài 34 Codelearn viet chương trình nhập vào một số và hiển thị phép nhân đến 5.
## While loop
n = int(input())
b = 1
while b <= 5:
    print(str(n) + " * " + str(b) + " =", n * b)
    b += 1
## For loop
n = int(input())
for i in range(1, 6):
    print(n, "*", i, "=", i * n)
    i += 1

# Bài 35 Codelearn viet chương trình đếm số chẵn lẻ.
a = int(input())
b = int(input())
count_odd = 0
count_even = 0

for i in range(a, b + 1):
    if i % 2 ==0:
        count_even += 1
    else:
        count_odd += 1
print("Number of even numbers:",count_even)
print("Number of odd numbers:",count_odd)

# Bài 36 Codelearn viet chương trình tính tổng n/(n+1).
n = int(input())
tong = 0
for i in range(1, n + 1):
    tong += i / (i + 1)
print(round(tong, 2))