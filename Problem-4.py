arr = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]

result = {}

for i in range(1, 10):  # 1 to 9
    count = 0
    for num in arr:
        if num % i == 0:
            count += 1
    result[i] = count

print(result)
