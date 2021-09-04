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
list = [2, 3 , 1, 5, 6]
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
print(s1[:2] + s2[2:])'''
s = "toi hoc python 2021"
r = s.split(" ")
print(r)
r.reverse()
print(" ".join(r))

