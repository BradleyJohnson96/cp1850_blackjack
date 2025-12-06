import db
import random
import sys

def display(hands_list):
    print("BLACKJACK!")
    print("Blackjack payout is 3:2\n")

def get_money():
    try:
        money = db.read_money(PLAYER_MONEY)
        return money
    except FileNotFoundError as e:
        print(e)
        print("Could not find datafile. Closing program")
        sys.exit()

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

def make_bet(money):
    print(f"Money: ${money}")
    if int(money) < 5:
        while True:
            try:
                more_chips = input("Would you like to by more chips? (y/n)?: ")
            except ValueError:
                print("Choice must be y/n, please try again.")
            if more_chips.lower() == "y":
                pass
                while True:
                    try:
                        chips = int(input("How many $ in chips would you like?: "))
                        money += chips
                        db.write_money(PLAYER_MONEY, str(money))
                        print(f"New balance: {money}")
                        break
                    except ValueError:
                        print("Must enter a number amount, try again.")
                        continue
                break
            elif more_chips.lower() == "n":
                print("Insufficient funds to continue. Closing program")
                sys.exit()
            else:
                print("Choice must be y/n, try again.")
    while True:
        try:
            bet = float(input("Bet amount: "))
            if bet > int(money):
                print(f"You only have ${money} in chips, try again.")
            else:
                if bet < 5 or bet > 1000:
                    print("Bet must be from 5-1000")
                else:
                    break
        except ValueError:
            print("Bet amount must be a number, please try again.")
    return bet

def hit_stand():
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

### All player functions ###

def player_cards(hands_list):
    print("\nYOUR CARDS:")
    for card in hands_list[1]:
        print(f"{card[0]} of {card[1]}")

def player_aces(hands_list):
    aces = 0
    for card in hands_list[1]:
        if card[0] == "Ace":
            aces += 1
    return aces

def player_value(hands_list):
    total = 0
    for card in hands_list[1]:
        total += card[2]
    return total

### All dealer functions ###

def show_hand(hands_list):
    print("\nDEALER'S SHOW CARD:")
    for card in hands_list[0]:
        print(f"{card[0]} of {card[1]}")

def dealers_cards(deck,hands_list):
    print("\nDEALER'S CARDS: ")
    card = deck.pop()
    hands_list[0].append(card)
    for card in hands_list[0]:
        print(f"{card[0]} of {card[1]}")

def dealer_aces(hands_list):
    aces = 0
    for card in hands_list[1]:
        if card[0] == "Ace":
            aces += 1
    return aces

def dealer_value(hands_list):
    total = 0
    for card in hands_list[0]:
        total += card[2]
    return total

PLAYER_MONEY = "money.txt"
def main():
    while True:
        money = get_money()
        deck = make_deck()
        # initialize dealer hand on top and player hand on bottom  #
        hands_list = [[deck.pop()],
            [deck.pop(), deck.pop()]
                 ]

        display(hands_list)
        bet = make_bet(money)
        money = get_money()
        show_hand(hands_list)
        player_cards(hands_list)
        player_points = player_value(hands_list)
        while True:
            if player_points > 21:
                break
            if hit_stand() == True:
                card = deck.pop()
                hands_list[1].append(card)
                player_cards(hands_list)
                p_aces = player_aces(hands_list)
                player_points = player_value(hands_list)
                # change ace value if bust #
                if player_points > 21:
                    for i in range(p_aces):
                        player_points -= 10
                        if player_points <= 21:
                            break
            else:
                break
        if player_points <= 21:
            dealers_cards(deck, hands_list)
            d_aces = dealer_aces(hands_list)
            dealer_points = dealer_value(hands_list)
            while dealer_points < 17:
                dealers_cards(deck, hands_list)
                dealer_points = dealer_value(hands_list)
                # change ace value if bust #
                if dealer_points > 21:
                    for i in range(d_aces):
                        dealer_points -= 10
                        if dealer_points <= 21:
                            break
            print()
            ### Check for dealer and player wins ###
            if dealer_points > 21:
                print("Dealer bust. You win!")
                money += bet
                print(f"Money: {round(money, 2)}")
                db.write_money(PLAYER_MONEY, str(money))
            elif dealer_points == player_points:
                print("Game is a tie. Returning bet.")
                print(f"Money: {round(money, 2)}")
            elif dealer_points > player_points:
                print("Sorry. You lose.")
                money -= bet
                print(f"Money: {round(money, 2)}")
                db.write_money(PLAYER_MONEY, str(money))
            elif dealer_points < player_points:
                if player_points == 21:
                    print("BLACKJACK")
                    print("You win! 1.5x bet amount")
                    money += bet * 1.5
                    print(f"Money: {round(money, 2)}")
                else:
                    print("You win!")
                    money += bet
                    print(f"Money: {round(money, 2)}")
                    db.write_money(PLAYER_MONEY, str(money))
        elif player_points > 21:
            print("\nSorry you bust. You lose.")
            money -= bet
            print(f"Money: {round(money, 2)}")
            db.write_money(PLAYER_MONEY, str(money))
        again = input("\nPlay again? (y/n): ")
        print()
        if again.lower() == "n":
            break
    print("Come back soon!")
    print("Bye")

if __name__=="__main__":
    main()