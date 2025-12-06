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

def show_hand(hands_list):
    print("\nDEALER'S SHOW CARD:")
    for card in hands_list[0]:
        print(f"{card[0]} of {card[1]}")

def player_cards(hands_list):
    print("\nYOUR CARDS:")
    for card in hands_list[1]:
        print(f"{card[0]} of {card[1]}")

def hit_stand(deck,hands_list):
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

def player_turn(deck,hands_list,player_points):
    while True:
        if player_points > 21:
            break
        if hit_stand(deck, hands_list) == True:
            card = deck.pop()
            hands_list[1].append(card)
            player_cards(hands_list)
            p_aces = player_aces(hands_list)
            player_points = player_value(hands_list)
            if player_points > 21:
                for i in range(p_aces):
                    player_points -= 10
                    if player_points <= 21:
                        break
        else:
            break

def dealers_cards(deck,hands_list):
    print("\nDEALER'S CARDS: ")
    card = deck.pop()
    hands_list[0].append(card)
    for card in hands_list[0]:
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

def win_calculator(money,bet,deck,hands_list,player_points):
    if player_points <= 21:
        dealers_cards(deck, hands_list)
        d_aces = dealer_aces(hands_list)
        dealer_points = dealer_value(hands_list)
        while dealer_points < 17:
            dealers_cards(deck, hands_list)
            dealer_points = dealer_value(hands_list)
            if dealer_points > 21:
                for i in range(d_aces):
                    player_points -= 10
                    if player_points <= 21:
                        break
        print()
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
        print("Sorry you bust. You lose.")
        money -= bet
        print(f"Money: {round(money, 2)}")
        db.write_money(PLAYER_MONEY, str(money))

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
        show_hand(hands_list)
        player_cards(hands_list)
        player_points = player_value(hands_list)
        player_turn(deck, hands_list, player_points)
        win_calculator(money, bet, deck, hands_list, player_points)
        again = input("\nPlay again? (y/n): ")
        print()
        if again.lower() == "n":
            break
    print("Come back soon!")
    print("Bye")

if __name__=="__main__":
    main()