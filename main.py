def summation(lst1, lst2):
    updated_list = [a + b for a, b in zip(lst1, lst2)]
    return updated_list

def find_min_max(lst):
    return min(lst), max(lst)

n = int(input("Input the value of n: "))

lst1 = []
print("Input lst1:")
for i in range(n):
    lst1.append(int(input()))

lst2 = []
print("Input lst2:")
for i in range(n):
    lst2.append(int(input()))


updated_list = summation(lst1, lst2)
print("Updated list from summation function:", updated_list)


min_val, max_val = find_min_max(updated_list)
print("Minimum and Maximum from find_min_max function:", (min_val, max_val))
