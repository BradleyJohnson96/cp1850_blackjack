import db
import random

def display():
    print("BLACKJACK!")
    print("Blackjack payout is 3:2\n")

def make_bet(money):
    print(f"Money: {money}")
    bet = float(input("Bet amount: "))
    return bet

def make_deck():
    suits = ["Clubs","Diamonds","Hearts","Spades"]
    ranks = ["Ace","Two","Three","Four","Five","Six","Seven",
        "Eight","Nine","Ten","Jack","Queen","King"]
    point_value = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] * 4
    deck = []
    for suit in suits:
        for rank,point in zip(ranks,point_value):
            deck.append(f"{rank} of {suit}")
    random.shuffle(deck)
    return deck

# def player_score(players_hand):
#     players_total = 0
#     for cards in players_hand:
#         players_total += cards[2]
#     return players_total
#
# def dealers_score(dealers_hand):
#     dealers_total = 0
#     for cards in dealers_hand:
#         dealers_total += cards[2]
#     return dealers_total


PLAYER_MONEY = "money.txt"
def main():
    money = db.read_money(PLAYER_MONEY)
    deck = make_deck()
    dealers_hand = [deck.pop()]
    players_hand = [deck.pop(), deck.pop()]
    display()
    bet = make_bet(money)






if __name__=="__main__":
    main()
