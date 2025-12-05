import db
import random
import sys

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
        try:
            choice = input("\nHit or Stand? (hit/stand): ")
            if choice.lower() == "hit":
                return True
            elif choice.lower() == "stand":
                return False
            else:
                print("Invalid choice, try again.")
        except ValueError:
            print("You must type hit/stand. Try again.")

def show_hand(hands):
    print("\nDEALER'S SHOW CARD:")
    for card in hands[0]:
        print(f"{card[0]} of {card[1]}")

def player_cards(hands):
    print("\nYOUR CARDS:")
    for card in hands[1]:
        print(f"{card[0]} of {card[1]}")

def dealers_cards(deck,hands):
    print("\nDEALER'S CARDS: ")
    card = deck.pop()
    hands[0].append(card)
    for card in hands[0]:
        print(f"{card[0]} of {card[1]}")

def make_deck():
    suits = ["Clubs","Diamonds","Hearts","Spades"]
    ranks = ["Ace","2","3","4","5","6","7",
        "8","9","10","Jack","Queen","King"]
    point_value = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] * 4
    deck = []
    for suit in suits:
        for rank,point in zip(ranks,point_value):
            deck.append([rank,suit,point])
    random.shuffle(deck)
    return deck

def player_aces(hands):
    aces = 0
    for card in hands[1]:
        if card[0] == "Ace":
            aces += 1
    return aces

def player_value(p_aces,hands):
    total = 0
    aces = 0
    for card in hands[1]:
        if card[0] == "Ace":
            aces += 1
        total += card[2]
    return total

def dealer_aces(hands):
    aces = 0
    for card in hands[1]:
        if card[0] == "Ace":
            aces += 1
    return aces

def dealer_value(d_aces,hands):
    total = 0
    for card in hands[0]:
        total += card[2]
    return total

PLAYER_MONEY = "money.txt"
def main():
    while True:
        try:
            money = db.read_money(PLAYER_MONEY)
        except FileNotFoundError as e:
            print(e)
            print("Could not find datafile. Closing program")
            sys.exit()
        deck = make_deck()
        hands = [[deck.pop()],
            [deck.pop(), deck.pop()]
                 ]
        display()
        bet = make_bet(money)
        show_hand(hands)
        player_cards(hands)
        p_aces = player_aces(hands)
        player_points = player_value(p_aces,hands)
        print(player_points)
        while True:
            if hit_stand(deck,hands) == True:
                card = deck.pop()
                hands[1].append(card)
                player_cards(hands)
                p_aces = player_aces(hands)
                player_points = player_value(p_aces, hands)
                print(player_points)
                print(p_aces)
            else:
                break
        dealers_cards(deck,hands)
        d_aces = dealer_aces(hands)
        dealer_value(d_aces,hands)
        again = input("Play again? (y/n): ")
        if again.lower() == "n":
            break
    print("Come back soon!")
    print("Bye")

if __name__=="__main__":
    main()