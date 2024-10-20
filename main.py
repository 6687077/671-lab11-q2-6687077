# YOUR CODE HERE
# Function สำหรับการทำ Element-wise addition ระหว่าง 2 lists
def summation(lst1, lst2):
    updated_list = [a + b for a, b in zip(lst1, lst2)]
    return updated_list

# Function สำหรับการหาค่าน้อยสุดและมากสุดใน list
def find_min_max(lst):
    return min(lst), max(lst)

# รับค่า n จากผู้ใช้
n = int(input("Input the value of n: "))

# รับค่า lst1 จากผู้ใช้
lst1 = []
print("Input lst1:")
for i in range(n):
    lst1.append(int(input()))

# รับค่า lst2 จากผู้ใช้
lst2 = []
print("Input lst2:")
for i in range(n):
    lst2.append(int(input()))

# เรียกใช้ฟังก์ชัน summation เพื่อคำนวณ updated_list
updated_list = summation(lst1, lst2)
print("Updated list from summation function:", updated_list)

# เรียกใช้ฟังก์ชัน find_min_max เพื่อหาค่าน้อยสุดและมากสุด
min_val, max_val = find_min_max(updated_list)
print("Minimum and Maximum from find_min_max function:", (min_val, max_val))
