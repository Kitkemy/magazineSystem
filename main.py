COMMANDS = "saldo", "zakup", "sprzedaż", "stop"

saldo = 1000.0

while True:
    action = input("podaj komendę:")    

    if action not in COMMANDS:
        print("niepoprawna komenda")
        continue
    if action == "stop":
        break

    if action == "saldo":
        amount = float(input("kwota salda: "))
        if amount < 0:
            if (amount < 0) and (saldo + amount < 0):
                print("za mało środków na koncie!")
                continue
        saldo = saldo + amount

    if action == "zakup":
        pass

    if action == "sprzedaż":
        pass
print(f"saldo: {saldo}")