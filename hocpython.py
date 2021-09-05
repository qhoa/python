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

# Bài 16 Codelearn nhập thông tin và tính toán, in ra kết quả của phép toán a và b

a = int(input())
b = int(input())
print("a + b = " + str(a + b))
print("a - b = " + str(a - b))
print("a * b = " + str(a * b))
print("a / b = " + str(a / b))
print("a % b = " + str(a % b))

# Bài 17 Codelearn nhập thông tin và tính toán, in ra kết quả hoán đổi của 2 giá trị a và b

a = int(input())
b = int(input())
c = a
a = b
b = c
print("after swap a = " + str(a) + ", b = " + str(b))

# Bài 18 Codelearn nhập thông tin và tính toán, in ra kết quả tính toán có số thập phân

r = float(input())
print("Circumference = " + str(2 * 3.14 * r))


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

# Bài 37 Codelearn học về mảng, array list
## (1) cấu trúc nhập số và gán vào mảng
n = int(input("Xin vui lòng nhập vào : ")) # nhập vào số lượng phần tử của mảng
list = []
for i in range(n):
    list.append(int(input())) # gán giá trị nhập vào từng phần tử của mảng
print(list)
## (2) tìm số nhỏ nhất trong mảng
n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))
nho_nhat = lst[0]
for i in lst:
    if i < nhonhat: # so sánh các phần tử với phần từ đầu tiên của mảng, nếu nhỏ hơn thì gán giá trị vào chính phần tử so sánh
        nho_nhat = i
print(nhonhat)

# Bài 38 Codelearn học về mảng, thực hành tính tổng các giá trị của mảng.
n = int(input("Nhập vào số phần tử của mảng: "))
list = []
tong = 0
for i in range(n):
    list.append(int(input()))
    tong += list[i]
print("Tổng giá trị các phần tử trong mảng = ", tong)

# Bài 39 Codelearn học về mảng, lý thuyết xắp xếp và bài tập.
''''
# 1. len () cho phép trả lại giá trị số lượng phần tử có trong mảng
list = [2, 3 , 1, 5, 6]
print(len(list))
# Đếm và liệt kê các phần tử trong mảng
for i in range(len(list)):
    print(list[i])
# 2. max() và min() phần tử trong mảng
print(max(list))
print(min(list))
# 3. insert() thêm giá trị vào trong mảng ( thêm giá trị 99 vào vị trí số 3 trong mảng )
list.insert(2, 99)
print(list)
# 4. remove() xóa phần tử trong mảng có giá trị 99.
list.remove(99)
print(list)
# 5. pop() xóa phần tử tại vị trí trong mảng.
list.pop(2)
print(list)
# 6. sort() xắp xếp các giá trị trong mảng
list.sort()
print(list)
list.sort(reverse=True)
print(list)
# 7. reverse() đảo ngược các phần tử trong mảng.
list.reverse()
print(list)
# 8. count() đếm phần tử được định nghĩa sẵn
print(list.count(2))
# 9. clear() xóa sạch
list.clear()
print(list)'''
## Bài tập liệt kê danh sách các phần tử mảng và sắp xếp theo thứ tự tăng dần
n = int(input())
list = []
for i in range(n):
    list.append(int(input()))
for i in list:
    list.sort()
    print(list)

# Bài 40 Codelearn viết chương trình in ra số lẻ trong mảng.
n = int(input())
odd_number = []
list = []
for i in range(n):
    list.append(int(input()))
for i in list:
    if i % 2 != 0:
        odd_number.append(i)
print(odd_number)

# Bài 41 Codelearn viết chương trình chia hết cho 5 và in ra trong chuỗi, nếu không có số nào thì trả lại kết quả [0]
n = int(input())
list = []
for i in range(n):
    list.append(int(input()))
div5 = []
for i in list:
    if i % 5 == 0:
        div5.append(i)
if len(div5) == 0:
    div5 = [0]
print(div5)

# Bài 42 Codelearn chuỗi string
# 1. len () đến tổng số lượng phần tử trong chuối
# 2. lower() chuyển toàn bộ upcase sang lowcase
s = "TOIHOCPYTHON"
print(s.lower())
# 3. upper() chuyển toàn bộ lower sang upper
c = "toihocpython"
print(s.upper())
# 4. isalnum() kiểm tra toàn bộ chuỗi là số hay chữ trả lại kết quả true / false
str = "Toihocpython2021"
print(str.isalnum())
str = "Toihocpython@2021"
print(str.isalnum())
# 5. isalpha kiểm tra toàn bộ chuối là chữ
print(str.isalpha())
# 6. isnumeric() kiểm tra toàn bộ chuỗi là số
print(str.isnumeric())
# 7. split() cắt chuỗi
spl = "Toi hoc python 2021"
print(spl.split(" "))
spl = "A1B1C1D1E1"
print(spl.split("1"))
# 8. join() ghép chuỗi
j = ['Toi', 'hoc', 'python', '2021']
print(" ".join(j))
print("-".join(j))
# 9. replace() thay thế chuỗi
r = "T0i h0c pyth0n"
print(r.replace("0", "o"))

# Bài 43 Codelearn nhập vào chuỗi in ra màn hình 2 ký tự đầu và 2 ký tự cuối của chuỗi.
s = input()
if len(s) >= 2:
    print(s[0:2] + s[-2] + s[-1])
    print(s[0:2] + s[-2:])
else:
    print("")

# Bài 44 Codelearn nhập vào 2 chuỗi, in ra màn hình đảo 2 ký tự đầu của 2 chuỗi và ghép lại
# "sun" "moon" = "mon suon"
s1 = input()
s2 = input()

r1 = s2[:2] + s1[2:]
r2 = s1[:2] + s2[2:]
print(r1 + " " + r2)

# Bài 45 Codelearn nhập vào chuỗi và đảo ngược lại toàn bộ phần tử của chuỗi. "this is a apple" ==> "apple a is this"
s = str(input())
r = s.split(" ") #Chuyển chuỗi sang mảng
r.reverse()  # đảo ngược sắp xếp lại giá trị của mảng
print(" ".join(r)) # ghép lại mảng thành chuỗi

# Bài 46 Codelearn học định nghĩa về hàm
## Định nghĩa hàm ví dụ
def show():
    for i in range(1, 11):
        print(i, end=" ") # end=" " có nghĩa hiển thị trên một dòng
#        print(i) # in xuống dòng
show()
## Viết hàm tỉnh tổng các phần tử trong mảng
def sum(lst): # hàm tính tổng các phần tử trong mảng
    tong = 0
    for i in lst:
        tong += i
    return tong
n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))
print(sum(lst))
#print()
#print(sum([1, 2, 3]))
#print(sum([4, 6 ,3]))

## Viết hàm đếm số chẵn trong mảng
def odd_number(lst):
    count = 0
    for i in lst:
        if i % 2 == 0:
            count += 1
    return count
lst = [2, 4, 8, 7, 9, 10]
print(odd_number(lst))
# Bài 47 Codelearn so sánh và bài tập
## Viết hàm nhập vào 3 số và so sánh số lớn nhất.
a = int(input())
b = int(input())
c = int(input())

def max_number(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c
print(max_number(a, b, c))

## Bài tập mở rộng viết hàm tìm số lớn nhất trong mảng
lst = [55, 6, 10, 3, 99]
def max_number(lst):
    max = lst[0]
    for i in lst:
        if i > max:
            max = i
    return max
print(max_number(lst))

# Bài 48 Codelearn viết hàm đếm chữ hoa , chữ thường trong chuỗi ký tự nhập vào từ bàn phím.
def count(s):
    count_lower = 0
    count_upper = 0
    for i in s:
        if i.islower():
            count_lower += 1
        elif i.isupper():
            count_upper += 1
    print("Given string:", s)
    print("Number of uppercase letters:", count_upper)
    print("Number of lowercase letters:", count_lower)

s = str(input())
count(s)

# Bài 49 Codelearn viết hàm tìm giá trị duy nhất.
def get_unique_values(lst):
    temp = []
    for i in lst:
        if i not in temp: # Sử dụng not in để kiểm tra phần tử có trong mảng tạm hay không.
            temp.append(i)
    return temp

n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))
print(get_unique_values(lst))

# Bài 50 Codelearn tìm số nguyên tố.
## Cách giải(1)
def is_prime(n):
    i = 1
    count = 0
    while i <= n:
        if n % i == 0:
            count += 1
        i += 1
    print(count)
    if count == 2:
        return True
    return False
n = int(input())
print(is_prime(n))

# Cách giải (2)
def is_prime(n):
    if n == 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    else:
        return True

n = int(input())
print(is_prime(n))

# Bài 51 thực hành Codelearn viết hàm tìm số chẵn
#Initial list
res = []

# Input lengths
lengths = int(input())

# Add element
for i in range(lengths):
    # Input elements
    n = int(input())
    res.append(n)


def evenNum(res):
    temp = []
    for i in res:
        if i % 2 == 0:
            temp.append(i)
    print(temp)

evenNum(res)

# Bài tập 52 Codelearn viết hàm tính bình phương của 2 số nhập vào ví dụ a , b = a^b
a = int(input())
b = int(input())

def power(a, b):
    c = 0
    c = a**b
    print(int(c))

power(a, b)

# Bài 53 Codelearn tìm ước số chung lớn nhất của 2 số nhập vào
a = int(input())
b = int(input())

def gcd(a,b):
    c = []
    res = []
    for i in range(1, a + 1):
        if a % i == 0:
            c.append(i)
    for n in range(1, b + 1):
        if b % n == 0 and n in c:
            res.append(n)
    print(res[-1])
gcd(a,b)

# Bài 54 Codelearn kiểm tra hình tam giác
a = int(input())
b = int(input())
c = int(input())

if a + b > c and a + c > b and b + c > a:
    if a == b and b == c:
        print("Equilateral triangle")
    elif a == b or b == c or a == c:
        print("Isosceles triangle")
    else:
        print("Scalene triangle")
else:
    print("không phải hình tam giác")
# Bài 55 Codelearn thực hành in ra màn hình chữ có hơn 3 ký tự trong 1 chuỗi nhập vào từ bàn phím
str = input()
def char(str):
    r = []
    for i in str.split(" "):
        if len(i) > 3:
            r.append(i)
    print(r)
char(str)

# Bài 56 Codelearn thực hành in ra màn hình chuyển mảng thành chuỗi liền nhau [3, 4, 5] => 345
#Initial list
res = []

# Input lengths
lengths = int(input())

# Add element
for i in range(lengths):
    # Input elements
    n = int(input())
    res.append(n)
for i in res:
    print(i, end="")

s = str(input())

# Bài 57 Codelearn thực hành in ra màn hình nếu 3 ký tự cuối là ing + ly, nếu nhỏ hơn 3 ký tự in ra màn hình, lớn hơn 3 ký tự + ing
def format(s):
    if len(s) >= 3:
        if s[-3:] in "ing":
            print(s + "ly")
        else:
            print(s + "ing")
    else:
        print(s)
format(s)

# Bài 58 Codelearn thực hành tính tổng các ước số của số nhập vào từ bàn phím 8 => 1 + 3 + 4 = 7
n = int(input())

def sumOfAll(n):
    res = []
    total = 0
    for i in range(1, n): # Bỏ qua giá trị n là chính mình loại bỏ kết quả  i = n và n % n = 0
        if n % i == 0:
            res.append(i)
    for i in res:
        total += i
    print(total)
sumOfAll(n)
# Bài 59 Codelearn thực hành tìm số dư, nguyên tắc của số dư là tổng các ước số lớn hơn chính nó.
n = int(input())

def is_abundant(n):
    res = []
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            res.append(i)
    for i in res:
        tong += i
    if tong > n:
        print("True")
    else:
        print("False")
is_abundant(n)