n = int(input("Введите натуральное число:\n"))

root = 1

while root * root < n:
    root += 1

if root * root == n:
    print(root)
else:
    print("Слишком сложно, не могу")
