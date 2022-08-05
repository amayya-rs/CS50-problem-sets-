num = [9, 1, 3, 6, 4]
n = 4

for i in range(n):
    for j in range(n):
        if num[j] > num[j + 1]:
            temp = num[j]
            num[j] = num[j + 1]
            num[j + 1] = temp
    n -= 1

print(num)