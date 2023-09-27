arr: list = input(
    "Введите целые числа, где каждый элемент в последовательности больше предыдущего: "
).split(" ")

exception: list = []

if len(arr) >= 2:
    for key, value in enumerate(arr):
        if key < (len(arr) - 1):
            # print(
            #     f"{int(arr[key + 1])} - {int(arr[key])} = {int(arr[key + 1]) - int(arr[key])}"
            # )
            difference: bool = (int(arr[key + 1]) - int(arr[key])) > 1
            if difference:
                exception.append(key + 1)
                # print(int(arr[key + 1]) - int(arr[key]))
    if len(exception) > 1:
        print("Ответ:", exception)
    elif len(exception) == 1:
        print("Ответ:", exception[0])
    else:
        print("Не найдено")
else:
    print("Массив меньше двух!")
