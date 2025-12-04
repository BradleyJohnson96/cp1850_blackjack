import db
import random

def display():
    print("BLACKJACK!")
    print("Blackjack payout is 3:2\n")

def make_bet(money):
    print(f"Money: {money}")
    if int(money) < 5:
        more_chips = input("Would you like to by more chips? (y/n)?")
        if more_chips.lower() == "y":
            chips = int(input("How many chips would you like?"))
            money = money + chips
            return money
        else:
            pass

    bet = float(input("Bet amount: "))
    return bet

def hit_stand(deck,hands):
    choice = input("Hit or Stand? (hit/stand): ")
    if choice.lower() == "hit":
        card = deck.pop()
        hands.append(card)
    elif choice.lower() == "stand":
        pass
    else:
        print("Invalid choice, try again.")

def show_hand(hands):
    print("\nDEALER'S SHOW CARD:")
    print(*hands[0])

def player_cards(hands):
    print("\nYOUR CARDS:")
    for card in hands[1]:
        print(card)

def dealers_cards(hands):
    print("\nDEALER'S CARDS: ")

    for card in hands[0]:
        print(card)

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

PLAYER_MONEY = "money.txt"
def main():
    while True:
        money = db.read_money(PLAYER_MONEY)
        deck = make_deck()
        hands = [[deck.pop()],
            [deck.pop(), deck.pop()]
                 ]
        display()
        bet = make_bet(money)
        show_hand(hands)
        player_cards(hands)
        #need hit/stand here
        dealers_cards(hands)
        again = input("Play again? (y/n): ")
        if again.lower() == "n":
            break
    print("Come back soon!")
    print("Bye")

if __name__=="__main__":
    main()