import random


def exhaustive_strategy(deck):
    return deck.running_totals[:-1]


def target_strategy(deck, target):
    i = 0
    while True:
        if i > len(deck.running_totals) - 1:
            return deck.running_totals[-1]
        if deck.running_totals[i] > target:
            return deck.running_totals[i]
        i += 1


def coin_flip_strategy(deck):
    positive_flips = 0
    expected_positive_flips = len(deck.net_integers) / 2  # odd length case? eg. 5 flips expect 2 or 3?
    i = 0
    print(deck.cards)
    print(deck.net_integers)
    print(deck.running_totals)
    while True:
        print(positive_flips)
        if i > len(deck.running_totals) - 1:
            return deck.running_totals[-1]
        if positive_flips >= expected_positive_flips:
            return deck.running_totals[i]
        if deck.net_integers[i] >= 0:  # treating 0 as a positive flip
            positive_flips += 1
        i += 1


def probability(deck, prob):
    i = 0
    while True:
        if i > len(deck.running_totals) - 1:
            return deck.running_totals[-1]
        random_choice = random.random()
        if random_choice < prob:
            i += 1
            continue
        else:
            return deck.running_totals[i]
