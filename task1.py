n = int(input("Введите целое число N: "))
arr: list = []


def list(n):
    if n > 0:
        if n % 3 == 0 or n % 5 == 0:
            arr.append(n)
    else:
        arr.reverse()
        arr.insert(0, 0)
        print(arr)
        return arr

    list(n - 1)


list(n)
