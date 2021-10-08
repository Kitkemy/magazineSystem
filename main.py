COMMANDS = "saldo", "zakup", "sprzedaż", "stop"

saldo = 1000.0

store = {
    "farba": {"count": 2, "price": 22.3},
    "wiadro": {"count": 10, "price": 4.5}
}

while True:
    action = input("podaj komendę:")    

    if action not in COMMANDS:
        print("niepoprawna komenda!")
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

    elif action == "zakup":
        product_name = input("Nazwa produktu: ")
        product_count = int(input("Ilość sztuk: "))
        product_price = float(input("Cena za sztukę: "))
        product_total_price = product_count * product_price
        if product_total_price > saldo:
            print(f"Cena za towary ({product_total_price}) przekracza wartość salda ({saldo})")
            continue
        else:
            saldo = saldo - product_total_price
            if not store.get(product_name):
                store[product_name] = {"count": product_count, "price": product_price}
            else:
                store_product_count = store[product_name]["count"]
                store[product_name] = {
                    "count": store_product_count + product_count,
                    "price": product_price}


print(f"saldo: {saldo}")
print(f"MAGAZYN: {store}")