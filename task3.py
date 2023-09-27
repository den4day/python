n: int = int(input("Введите число N: "))
arr: list = []

for value in range(n + 1):
    arr.append(value**2)

arr.reverse()

for value in range(n):
    arr.append((value + 1) ** 2)

print(arr)
