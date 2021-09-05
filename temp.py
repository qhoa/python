'''n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))
nhonhat = lst[0]
for i in lst:
    if i < nhonhat:
        nhonhat = i
print(nhonhat)'''
# Tạo ra list để lưu trữ các số nguyên
list1 = [1, 2, 3]
# Tạo ra list để lưu trữ các xâu ký tự
list2 = ["Viet", "Tuan", "Duong"]
# Bạn cũng có thể tạo ra một list lưu trữ các kiểu dữ liệu khác nhau
list3 = [7, 3.5, "Codelearn"]
'''for i in list1:
    print(i)
for i in list2:
   print(i)'''
'''n = int(input("Xin vui lòng nhập vào : "))
list = []
for i in range(n):
    list.append(int(input()))
print(list)
nhonhat = list[0]
for i in list:
    if i < nhonhat:
        nhonhat = i
print(nhonhat)'''
'''n = int(input("Nhập vào số phần tử của mảng: "))
list = []
tong = 0
for i in range(n):
    list.append(int(input()))
    tong += list[i]
print("Tổng giá trị các phần tử trong mảng = ", tong)'''
# len () cho phép trả lại giá trị số lượng phần tử có trong mảng
list = [2, 3, 1, 5, 6]
'''print(len(list))
# Đếm và liệt kê các phần tử trong mảng
for i in range(len(list)):
    print(list[i])
# max() và min() phần tử trong mảng
print(max(list))
print(min(list))
# insert() thêm giá trị vào trong mảng ( thêm giá trị 99 vào vị trí số 3 trong mảng )
list.insert(2, 99)
print(list)
# remove() xóa phần tử trong mảng có giá trị 99.
list.remove(99)
print(list)
# pop() xóa phần tử tại vị trí trong mảng.
list.pop(2)
print(list)
# sort() xắp xếp các giá trị trong mảng
list.sort()
print(list)
list.sort(reverse=True)
print(list)
# reverse() đảo ngược các phần tử trong mảng.
list.reverse()
print(list)
# count() đếm phần tử được định nghĩa sẵn
print(list.count(2))
# clear() xóa sạch
list.clear()
print(list)
## Bài tập liệt kê danh sách các phần tử mảng và sắp xếp theo thứ tự tăng dần
n = int(input())
list = []
for i in range(n):
    list.append(int(input()))
for i in list:
    list.sort()
    print(list)'''
'''n = int(input())
list = []
for i in range(n):
    list.append(int(input()))
list = [2, 3, 1, 5, 6]
kq = []
for i in list:
    if i % 2 != 0:
        kq.append(i)
print(kq)
n = int(input())
result = []
list = []
for i in range(n):
    list.append(int(input()))
for i in list:
    if i % 2 != 0:
        result.append(i)
print(result)
n = int(input())
list = []
for i in range(n)
    list.append(int(input()))
lst = [2, 3 , 1, 6, 5]
d5 = []
for i in lst:
    if i % 5 == 0:
        d5.append(i)
    elif i % 5 != 0:
print(d5)
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
s = input()
if len(s) >= 2:
    print(s[0:2] + s[-2] + s[-1])
    print(s[0:2] + s[-2:])
else:
    print("")
print(s[0])
print(s[0:3])
print(s[-1])
print(s[0:-7])
print(s[-2])
print(s[0:2] + s[-2] + s[-1])
print(s1[0:2] + s1[-2] + s1[-1])
print(s2[0:2] + s2[-2] + s2[-1])
s1 = "apple"
s2 = "banana"
print(s2[:2] + s1[2:])
print(s1[:2] + s2[2:])
s = "toi hoc python 2021"
r = s.split(" ")
print(r)
r.reverse()
print(" ".join(r))

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
# Viết hàm đếm số chẵn trong mảng nhập vào
def odd_number(lst):
    count = 0
    for i in lst:
        if i % 2 == 0:
            count += 1
    return count
lst = [2, 4, 8, 7, 9, 10]
print(odd_number(lst))
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
lst = [55, 6, 10, 3, 99]
def max_number(lst):
    max = lst[0]
    for i in lst:
        if i > max:
            max = i
    return max
print(max_number(lst))
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
## Bài tập 49
Write a function that takes a list as an argument and returns a list containing unique values that appear in the list.

Example:

For lst = [1,2,3,3,3,3,4,5], the output should be [1,2,3,4,5]
For lst = [1,1,2,2,3,3,3,3,4,4,4,4,5,5], the output should be [1,2,3,4,5]
For lst = [1, 1, 1], the output should be [1]
lst = [1,2,3,3,3,3,4,5]
temp = []
for i in lst:
    if i not in temp:
        temp.append(i)
print(temp)
# Bài 50
Write a Python program that accepts a natural number n from the user and checks whether that number is a prime number. If n is a prime number, return True, return False otherwise. 

A prime number (or a prime) is a natural number greater than 1 that is not a product of two smaller natural numbers. 2, 3, 5, 7, 11, 13, 17,... are prime numbers.

Example

For n = 9, the output should be False
For n = 3, the output should be True
def is_prime(n):
    if n == 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    else:
        return True

n = int(input())
print(is_prime(n))

def is_prime(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    if count == 2:
        return True
    return False


n = int(input())
print(is_prime(n))
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
    for a in res:
        if a % 2 == 0:
            temp.append(a)
    print(temp)

evenNum(res)
a = int(input())
b = int(input())

def power(a, b):
    c = 0
    c = a**b
    print(int(c))
power(a, b)
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
str = "The quick brown fox jumps over the lazy dog"
#r = str.split(" ")
def char(str):
    r = []
    for i in str.split(" "):
        if len(i) > 3:
            r.append(i)
    print(r)
char(str)
#Initial list
res = []

# Input lengths
lengths = int(input())

# Add element
for i in range(lengths):
    # Input elements
    res.append(int(input()))

for i in res:
    print(i, end="")
s = str(input())

def format(s):
    if len(s) >= 3:
        if s[-3:] in "ing":
            print(s + "ly")
        else:
            print(s + "ing")
    else:
        print(s)
format(s)'''
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
