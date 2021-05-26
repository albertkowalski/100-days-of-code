import random
import art

print(art.logo)
player_cards = []
dealer_cards = []


def show_card(card_index):
    cards = ["A", 2, 3, 4, 5, 6, 7, 8, 9, "T", "J", "Q", "K"]
    return cards[card_index]


def get_card_index():
    return random.randint(0, 12)


def get_card_value(card_index):
    values = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card_value = values[card_index]
    return card_value


def get_hand_value(cards):
    cards_value = 0
    aces = cards.count(0)
    for card in cards:
        if not card == 0:
            cards_value += get_card_value(card)
    if cards_value <= 21 - aces and aces > 0:
        if cards_value + (aces - 1) + get_card_value(0) <= 21:
            cards_value += + aces + 10
        else:
            cards_value += aces
    return cards_value


def show_hand(hand):
    cards = []
    for card in hand:
        cards.append(show_card(card))
    print(*cards)



def initial_deal():
    player_cards.append(get_card_index())
    player_cards.append(get_card_index())
    dealer_cards.append(get_card_index())
    dealer_cards.append(get_card_index())


initial_deal()
show_hand(player_cards)
print(get_hand_value(player_cards))