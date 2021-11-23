import random
# 11 = J, 12 = Q, 13 = K, 14 = A
card_values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
suits = ["clubs", "diamonds", "hearts", "spades"]

face_cards = {
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14,
    11: "J",
    12: "Q",
    13: "K",
    14: "A"
}
class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

def generate_cards():
    cards = []
    for value in card_values:
        for suit in suits:
            if value in face_cards:
                _card = Card(face_cards[value], suit)
            else:
                _card = Card(value, suit)
            cards.append(_card)
    return cards

cards = generate_cards()

def deal_card(cards):
    i = random.randint(0, len(cards)-1)
    card = cards[i]
    cards.pop(i)
    return card, cards

def deal(cards = cards, num_opp = 2):
    opp_hands = []
    for _ in range(num_opp):
        card1, cards = deal_card(cards)
        card2, cards = deal_card(cards)
        opp_hands.append([card1, card2])
    card1, cards = deal_card(cards)
    card2, cards = deal_card(cards)
    your_hand = [card1, card2]
    return your_hand, opp_hands

your_hand, opp_hands = deal()
print(f"Your hand: {[(card.value, card.suit) for card in your_hand]}")
# print(opp_hands)
# flop
# turn
# river
def flop(cards=cards):
    card1, cards = deal_card(cards)
    card2, cards = deal_card(cards)
    card3, cards = deal_card(cards)
    return [card1, card2, card3]

def table_deal(cards=cards):
    card, cards = deal_card(cards)
    return card

table = flop()
print(f"Cards on the table: {[(card.value, card.suit) for card in table]}")
table.append(table_deal())
print(f"Cards after turn: {[(card.value, card.suit) for card in table]}")
table.append(table_deal())
print(f"Cards after river: {[(card.value, card.suit) for card in table]}")

"""
evaluates one hand and the table
returns the evaluated hand
(high, pair, 2 pair, 3 kind, straight, flush, full house, quads, straight flush)
"""
def evaluate(hand, table):
    total_hand = hand + table
    # count values and suit
    counts = {}
    suits = {}
    vals = set()
    # loop through all the cards
    for card in total_hand:
        if card.value in face_cards:
            card_value = face_cards[card.value]
        else:
            card_value = card.value
        vals.add(card_value)
        if card_value in counts:
            counts[card_value] += 1
        else:
            counts[card_value] = 1
        if card.suit in suits:
            suits[card.suit] += 1
        else:
            suits[card.suit] = 1
    # sort counts and suits
    sorted_counts = sorted(counts.items(), key=lambda item:(item[1], item[0]), reverse=True)
    sorted_suits = sorted(suits.items(), key=lambda item:(item[1], item[0]), reverse=True)

    # check if vals contains a straight
    run = [sorted(list(vals))[0]]
    lastval = sorted(list(vals))[0]
    is_straight = False
    for val in sorted(list(vals)):
        if val - lastval == 1:
            run.append(val)
        else:
            run = [val]
        lastval = val
        if len(run) == 5:
            is_straight = True
            break
        # print(f"last val: {lastval}")
        # print(f"run: {run}")
    
    # check if sorted_suits contains a flush
    is_flush = False
    if sorted_suits[0][1] == 5:
        is_flush = True
    # check for straight flush
    if is_straight:
        if is_flush:
            return "Straight Flush!"
    if sorted_counts[0][1] == 4:
        return f"Quad {face_cards.get(sorted_counts[0][0]) if sorted_counts[0][0] in face_cards else sorted_counts[0][0]}s!"
    if sorted_counts[0][1] == 3:
        if sorted_counts[1][1] == 2:
            return f"Full house {face_cards.get(sorted_counts[0][0]) if sorted_counts[0][0] in face_cards else sorted_counts[0][0]}s over {face_cards.get(sorted_counts[1][0]) if sorted_counts[1][0] in face_cards else sorted_counts[1][0]}s!"
    if is_flush:
        return f"Flush in {face_cards.get(sorted_counts[0][0]) if sorted_counts[0][0] in face_cards else sorted_counts[0][0]}!"
    if is_straight:
        return f"Straight! {run}"
    # check for groups
    # print(sorted_counts)
        
    if sorted_counts[0][1] == 3:
        return f"Triple {face_cards.get(sorted_counts[0][0]) if sorted_counts[0][0] in face_cards else sorted_counts[0][0]}s!"
    if sorted_counts[0][1] == 2:
        if sorted_counts[1][1] == 2:
            return f"Two pair {face_cards.get(sorted_counts[0][0]) if sorted_counts[0][0] in face_cards else sorted_counts[0][0]} and {face_cards.get(sorted_counts[1][0]) if sorted_counts[1][0] in face_cards else sorted_counts[1][0]}!"
        else:
            return f"Pair of {face_cards.get(sorted_counts[0][0]) if sorted_counts[0][0] in face_cards else sorted_counts[0][0]}!"
    if sorted_counts[0][1] == 1:
        return f"High Card {face_cards.get(sorted_counts[0][0]) if sorted_counts[0][0] in face_cards else sorted_counts[0][0]}!"
    # print(sorted_suits)
    
"""
takes your hand, the opponents hands, and the cards on the table
determines the values
returns a winner with all values shown
"""
def determine(hand, opp_hands, table):
    print(f"Your highest poker hand: {evaluate(hand, table)}")
    for opp in opp_hands:
        print(f"Opponent hand: {opp[0].value} {opp[0].suit}, {opp[1].value} {opp[1].suit}")
        print(f"Your opponents highest poker hand: {evaluate(opp, table)}")

determine(your_hand, opp_hands, table)

# TODO: make sure evaluate doesn't return the same value for everyone
#       by disqualifying hands that can be made from the table only
# 1. create a real matcher
# 2. there's 5C3 = 10 possible hands
# 3. select the highest from those hands
# TODO: implement betting
# 1. allow "bets", "calls", and "knocks" after each card deal
# 2. make opponent bets after each card deal
# 3. keep track of total pile
# TODO: implement rotations
# 1. small blind, big blind, dealer
# 2. changing possible number of opponents
# TODO: implement smart betting for computer
# TODO: logic to decide winner
    