ranks = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
suits = ("Hearts", "Diamonds", "Clubs", "Spades")
cards = []

# TODO: Create every possible pairing of ranks and suits
#   And add it to the empty list of cards
""" 

    A of Hearts
    2 of Hearts
    3 of Hearts
    ...
    K of Hearts
    A of Diamonds
    2 of Diamonds
    3 of Diamonds
    ...
"""
for suit in suits:
    print()
    for rank in ranks:
        print(rank, suit)
        cards.append(f"{rank} {suit}")

print()
print(cards)
print()
print(f"Total cards is {len(cards)}")