# Toi hoc python
print("Toi hoc python, python case sensitive")
print("Ngon ngu lap trinh nhay cam qua")

# Dat bien nhu an keo
a = 3
b = 4
print(a+b)
print(a*b)
print(a/b)
c = a + b
print(c)

# Bài 32 Codelearn kiến thức vòng lặp while.
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
#Break cho phép dừng, thoát vòng lặp khi match điều kiện
for i in range(1, 11):
    if i == 6:
        break
    print(i)
#Continue cho phép tiếp tục vòng lặp khi match điều kiện
for i in range(1, 20):
    if i % 2 == 0:
        continue
    print(i)
'''
## Bài tập (1) in ra toàn bộ ký tự với từ nhập vào là "sunny"
s = input()
for c in s:
    if c == 'y':
        print("Current character:", c)