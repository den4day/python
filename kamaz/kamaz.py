from import_this import RACE_DATA

if __name__ == "__main__":
    winner: str = ""

    for n in RACE_DATA.values():
        if n.get("FinishedPlace") == 1:
            winner = f'Выиграл - {n.get("RacerName", "-1").upper()}!!! Поздравляем!!'
            break

    winner += "\n" + "_" * len(winner)
    print(winner)

    print("")
    print("Первые три места:")
    print("")

    print("Гонщик на 1 месте:")

    def seconds_conversion(sec):
        h = str(sec // 3600)
        if len(h) < 2:
            h = "0" + h
        m = str((sec % 3600) // 60)
        if len(m) < 2:
            m = "0" + m
        s = str(sec % 60)
        if len(s) < 2:
            s = "0" + s
        return h + ":" + m + ":" + s

    for i in RACE_DATA.values():
        if i.get("FinishedPlace") == 1:
            first_winnerName = f'Имя: {i.get("RacerName")}'
            break
    for i2 in RACE_DATA.values():
        if i2.get("FinishedPlace") == 1:
            first_winnerTeam = f'Команда: {i2.get("RacerTeam")}'
            break
    for i3 in RACE_DATA.values():
        if i3.get("FinishedPlace") == 1:
            first_winnerTime = (
                f'Время: {seconds_conversion(i3.get("FinishedTimeSeconds"))}'
            )
            break

    print("   ", first_winnerName)
    print("   ", first_winnerTeam)
    print("   ", first_winnerTime)

    print("")

    print("Гонщик на 2 месте:")

    for k in RACE_DATA.values():
        if k.get("FinishedPlace") == 2:
            second_winnerName = f'Имя: {k.get("RacerName")}'
            break
    for k2 in RACE_DATA.values():
        if k2.get("FinishedPlace") == 2:
            second_winnerTeam = f'Команда: {k2.get("RacerTeam")}'
            break
    for k3 in RACE_DATA.values():
        if k3.get("FinishedPlace") == 2:
            second_winnerTime = (
                f'Время: {seconds_conversion(k3.get("FinishedTimeSeconds"))}'
            )
            break

    print("   ", second_winnerName)
    print("   ", second_winnerTeam)
    print("   ", second_winnerTime)

    print("")

    print("Гонщик на 3 месте:")

    for r in RACE_DATA.values():
        if r.get("FinishedPlace") == 3:
            third_winnerName = f'Имя: {r.get("RacerName")}'
            break
    for r2 in RACE_DATA.values():
        if r2.get("FinishedPlace") == 3:
            third_winnerTeam = f'Команда: {r2.get("RacerTeam")}'
            break
    for r3 in RACE_DATA.values():
        if r3.get("FinishedPlace") == 3:
            third_winnerTime = (
                f'Время: {seconds_conversion(r3.get("FinishedTimeSeconds"))}'
            )
            break
    print("   ", third_winnerName)
    print("   ", third_winnerTeam)
    print("   ", third_winnerTime)

    print("")
