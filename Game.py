# make an interactive with tkinter?

import random


class Deck:
    def __init__(self):
        self.cards = list(range(1, 14)) * 4  # pass in cards parameter if working general case
        random.shuffle(self.cards)
        # prevent crash if given deck size odd when working in general case
        if len(self.cards) % 2 == 1:
            self.cards = self.cards[:-1]
        self.net_integers = []
        self.running_totals = []
        total = 0
        i = 0
        while i < len(self.cards):
            self.net_integers.append(self.cards[i] - self.cards[i + 1])
            i += 2
        i = 0
        while i < len(self.net_integers):
            total += self.net_integers[i]
            self.running_totals.append(total)
            i += 1


def single_trial(show_calculations):
    deck = Deck()
    if show_calculations is True:
        print(deck.cards)
        print(deck.net_integers)
        print(deck.running_totals)
    return max(deck.running_totals)


""" This outputs 16, on average, for number_of_trials large. (like 1 million)
I call this naive because this doesn't prove +16 is the target."""


def naive_averages_test(number_of_trials):
    sum_of_maximums = 0
    i = 0
    while i < number_of_trials:
        sum_of_maximums += single_trial(False)
        i += 1
    print(sum_of_maximums / number_of_trials)

