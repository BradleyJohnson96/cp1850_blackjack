import db
import random

PLAYER_MONEY = "money.txt"
def make_deck():
    suits = ["Clubs","Diamonds","Hearts","Spades"]
    ranks = ["Ace","Two","Three","Four","Five","Six","Seven",
        "Eight","Nine","Ten","Jack","Queen","King"]
    point_value = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] * 4

    deck = []

    for suit in suits:
        for rank,point in zip(ranks,point_value):
            deck.append(f"{rank} of {suit}")

    print(deck)
def main():
    money = db.read_money(PLAYER_MONEY)
    make_deck()

    dealers_hand = []
    players_hand = []

if __name__=="__main__":
    main()
