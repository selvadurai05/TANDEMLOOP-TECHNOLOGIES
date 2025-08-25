n = int(input("Enter a number: "))
result = []

if n % 2 == 0:  # Even
    limit = n - 1
else:  # Odd
    limit = n

for i in range(limit):
    result.append(2 * i + 1)

print(", ".join(map(str, result)))
