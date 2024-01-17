from random import shuffle

deck = [x for x in range(52)]
suits_lst = ["Spades", "Hearts", "Diamonds", "Clubs"]
ranks_lst = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

shuffle(deck)

for i in range(4):  # Prints first 4 shuffled cards
    suit = suits_lst[deck[i] // 13]  # Gets a number from deck (Card Num) and int division for suit
    rank = ranks_lst[deck[i] % 13]  # Gets the exact num of card
    print("Card Num", deck[i], "is the", rank, "of", suit)
