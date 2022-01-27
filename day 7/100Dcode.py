import random
word_list = ['avocado', 'scene', 'standard', 'purchase', 'suffer', 'japan']
# TODO-1 Randomly Choose a word From the word_list
#  and assign it to a variable called chosen_word
# TODO-2 Ask the user to Guess a letter and
#  assign their answer variable called Guess. make guess lowercase
# TODO-3 check i one of the letters in the guess are the ones in the word list

chosen_word = random.choice(word_list)
guess_letter = str(input("Guess a letter: ")).lower()
print(chosen_word)


# def checker(a, b):
#     word_separate = []
#     number_blanks = ['_'] * len(word_separate)
#     for i in range(0, len(a)):
#         word_separate.append(chosen_word[i])
#     #   print(word_separate)
#     for i in range(0, len(a)):
#         if b == word_separate[i]:
#             number_blanks[i] += word_separate[i]
#                 # print("right")
#             # elif b != word_separate[i]:
#             #     print("wrong")
#         if b in word_separate:
#             print("right")
#         elif b not in word_separate:
#             print("wrong")
#         print(number_blanks)

# chosen_word = random.choice(word_list)








word_separate = []
guess_letter = str(input("Guess a letter: ")).lower()
for i in range(0, len(chosen_word)):
    word_separate.append(chosen_word[i])
    print(word_separate)
number_blanks = ['_'] * len(word_separate)
for i in range(0, len(chosen_word)):
    if guess_letter == word_separate[i]:
        number_blanks[i] = word_separate[i]
        print("right")
    elif guess_letter != word_separate[i]:
        print("wrong")

