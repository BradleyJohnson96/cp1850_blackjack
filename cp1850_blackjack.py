PLAYER_MONEY = "money.txt"

def read_money():
    with open(PLAYER_MONEY, "r") as file:
        money = file.read()
        return money

def write_money(money):
    with open(PLAYER_MONEY, "w") as file:
        file.write(money)

def main():
    suit = []
    rank = []
    pint_value = []
    dealers_hand = []
    players_hand = []
    money = read_money()
    print(money)

if __name__=="__main__":
    main()
