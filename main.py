numbers = [6, 5, 8, 1, 7]
n = len(numbers) - 1

for i in range(n):
    for j in range(n):
        if numbers[j] > numbers[j + 1]:
            temp = numbers[j]
            numbers[j] = numbers[j + 1]
            numbers[j + 1] = temp
    n = n - 1

print(numbers)