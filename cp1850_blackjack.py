import db

PLAYER_MONEY = "money.txt"

def main():
    money = db.read_money(PLAYER_MONEY)

    cards = [["Clubs","Diamonds","Hearts","Spades"],
        ["Ace","Two","Three","Four","Five","Six","Seven",
        "Eight","Nine","Ten","Jack","Queen","King"],
        [1, 2, 3, 4, 5, 6,7, 8, 9, 10, 10, 10, 10]]

    dealers_hand = []
    players_hand = []
    


if __name__=="__main__":
    main()
