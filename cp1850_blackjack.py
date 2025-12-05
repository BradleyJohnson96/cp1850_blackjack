import db
import random

def display():
    print("BLACKJACK!")
    print("Blackjack payout is 3:2\n")

def make_bet(money):
    print(f"Money: ${money}")
    if int(money) < 5:
        more_chips = input("Would you like to by more chips? (y/n)?: ")
        if more_chips.lower() == "y":
            chips = int(input("How many $ in chips would you like?: "))
            money += chips
            db.write_money(PLAYER_MONEY, str(money))
            return money
        else:
            pass
    while True:
        bet = float(input("Bet amount: "))
        if bet > int(money):
            print(f"You only have ${money} in chips, try again.")
        else:
            if bet < 5 or bet > 1000:
                print("Bet must be from 5-1000")
            else:
                break
    return bet

def hit_stand(deck,hands):
    while True:
        choice = input("\nHit or Stand? (hit/stand): ")
        if choice.lower() == "hit":
            return True
        elif choice.lower() == "stand":
            return False
        else:
            print("Invalid choice, try again.")

def show_hand(hands):
    print("\nDEALER'S SHOW CARD:")
    print(*hands[0])

def player_cards(hands):
    print("\nYOUR CARDS:")
    for card in hands[1]:
        print(card)

def dealers_cards(deck,hands):
    print("\nDEALER'S CARDS: ")
    card = deck.pop()
    hands[0].append(card)
    for card in hands[0]:
        print(card)

def make_deck():
    suits = ["Clubs","Diamonds","Hearts","Spades"]
    ranks = ["Ace","2","3","4","5","6","7",
        "8","9","10","Jack","Queen","King"]
    point_value = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] * 4
    deck = []
    for suit in suits:
        for rank,point in zip(ranks,point_value):
            deck.append(f"{rank} of {suit}")
    random.shuffle(deck)
    return deck

def card_value(hands):
    pass

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
        while True:
            if hit_stand(deck,hands) == True:
                card = deck.pop()
                hands[1].append(card)
                player_cards(hands)
            else:
                break
        dealers_cards(deck,hands)
        again = input("Play again? (y/n): ")
        if again.lower() == "n":
            break
    print("Come back soon!")
    print("Bye")

if __name__=="__main__":
    main()