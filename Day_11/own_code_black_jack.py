import random
from art import logo
from replit import clear


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(insert_card):
    if sum(insert_card) == 21 and len(insert_card) == 2:
        return 0
    if 11 in insert_card and sum(insert_card) > 21:
        insert_card.remove(11)
        insert_card.append(1)
    return sum(insert_card)


def compare(user, computer):
    if user == computer:
        return "Draw 🙃"
    elif computer == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user == 0:
        return "Win with a Blackjack 😎"
    elif user > 21:
        return "You went over. You lose 😭"
    elif computer > 21:
        return "Opponent went over. You win 😁"
    elif user > computer:
        return "You win 😃"
    else:
        return "You lose 😤"


def play_game():
    print(logo.logo)

    is_game_over = False
    user_cards = []
    computer_cards = []

    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f'USER CARDS: {user_cards} \n'
              f'COMPUTER CARDS: {computer_cards}')
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            response = input("type Y to Draw another card \n"
                             "type N to Pass \n"
                             "enter your answer here: ")
            if response.lower() == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True
                pass

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(f" Your final hand: {user_cards}, \n"
          f" final score: {user_score}")
    print(f" Computer's final hand: {computer_cards}, \n"
          f" final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear()
    play_game()
