import random


is_game_over = False
user_cards = []
computer_cards = []


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        print("Black Jack")
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


for i in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())


print(f'computer cards: {computer_cards} \n'
      f'user cards: {user_cards}')

user_score = calculate_score(user_cards)
computer_score= calculate_score(computer_cards)

while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score= calculate_score(computer_cards)

    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True
    else:
        user_should_deal = input('type y to get another card \n'
                                 'type n to pass: \n'
                                 '')
        if user_should_deal.lower() == 'y':
            user_cards.append(deal_card())
        else:
            is_game_over = True
            pass

    print(f'computer score: {computer_score} \n'
          f' user score: {user_score}')

while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = computer_score(computer_cards)



print(f'computer cards: {computer_cards} \n'
      f' user cards: {user_cards}')
