def nod(a: int = 0, b: int = 0):
    if a <= 0 or b <= 0:
        return 0

    while b != 0:
        remainder = a % b
        a = b
        b = remainder

    return a


print(nod(150, 84))
