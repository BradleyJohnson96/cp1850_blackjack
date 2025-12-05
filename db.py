def read_money(PLAYER_MONEY):
    try:
        with open(PLAYER_MONEY, "r") as file:
            money = file.read()
            return float(money)
    except FileNotFoundError:
        print("Player money file not found!")


def write_money(PLAYER_MONEY,money):
    with open(PLAYER_MONEY, "w") as file:
        file.write(money)