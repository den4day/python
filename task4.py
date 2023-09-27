player1, player2 = input("Ввод: ").split(" ")

if player1 == "камень" and player2 == "ножницы":
    print("игрок 1 выиграл")
elif player1 == "ножницы" and player2 == "камень":
    print("игрок 2 выиграл")
elif player1 == "камень" and player2 == "бумага":
    print("игрок 2 выиграл")
elif player1 == "бумага" and player2 == "камень":
    print("игрок 1 выиграл")
elif player1 == "камень" and player2 == "камень":
    print("ничья")
elif player1 == "ножницы" and player2 == "бумага":
    print("игрок 1 выиграл")
elif player1 == "бумага" and player2 == "ножницы":
    print("игрок 2 выиграл")
elif player1 == "ножницы" and player2 == "ножницы":
    print("ничья")
elif player1 == "бумага" and player2 == "бумага":
    print("ничья")
