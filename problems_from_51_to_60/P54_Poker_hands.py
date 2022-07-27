from urllib.request import urlopen
from collections import Counter


class Hand():
    def __init__(self, hand):
        self.values = [hand[0], hand[2], hand[4], hand[6], hand[8]]
        self.values = self.translate_in_integers(self.values)
        self.suits = [hand[1], hand[3], hand[5], hand[7], hand[9]]

    def translate_in_integers(self, values):
        translated_version = list()
        excpetion_values = {"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
        for value in values:
            try:
                translated_version.append(int(value))
            except ValueError:
                translated_version.append(excpetion_values[value])
        return translated_version


class poker_hands():
    wins_player_1 = 0

    def __init__(self):
        self.hands = self.get_hands(
            "https://projecteuler.net/project/resources/p054_poker.txt")

    def get_hands(self, url):
        textpage = urlopen(url)
        text = str(textpage.read(), 'utf-8')
        text = text.split("\n")
        text.pop()
        return text

    def solution(self):
        for _10_cards in self.hands:
            self.separate_hands(_10_cards)
            rank_player_1, self.number_to_check_if_tie_player_1 = self.get_rank_and_tie_number(
                self.hand_player_1)
            rank_player_2, self.number_to_check_if_tie_player_2 = self.get_rank_and_tie_number(
                self.hand_player_2)
            if rank_player_1 > rank_player_2:
                self.wins_player_1 += 1
            if rank_player_1 == rank_player_2:
                self.handle_tie()
        return self.wins_player_1

    def separate_hands(self, _10_cards):
        _10_cards = _10_cards.replace(" ", "")
        self.hand_player_1 = Hand(_10_cards[:10])
        self.hand_player_2 = Hand(_10_cards[10:])

    def get_rank_and_tie_number(self, hand):
        if self.royal_flush(hand):
            number_to_check_if_tie = 14
            return 10, number_to_check_if_tie

        if self.straight_flush(hand):
            number_to_check_if_tie = max(hand.values)
            return 9, number_to_check_if_tie

        if self.four_of_a_kind(hand):
            number_to_check_if_tie = [key for key, value in Counter(
                hand.values).items() if value == 4][0]
            return 8, number_to_check_if_tie

        if self.full_house(hand):
            number_to_check_if_tie = [key for key, value in Counter(
                hand.values).items() if value == 3][0]
            return 7, number_to_check_if_tie

        if self.flush(hand):
            number_to_check_if_tie = max(hand.values)
            return 6, number_to_check_if_tie

        if self.straight(hand):
            number_to_check_if_tie = max(hand.values)
            return 5, number_to_check_if_tie

        if self.three_of_a_kind(hand):
            number_to_check_if_tie = [key for key, value in Counter(
                hand.values).items() if value == 3][0]
            return 4, number_to_check_if_tie

        if self.two_pairs(hand):
            number_to_check_if_tie = max(
                [key for key, value in Counter(hand.values).items() if value == 2])
            return 3, number_to_check_if_tie

        if self.one_pair(hand):
            number_to_check_if_tie = [key for key, value in Counter(
                hand.values).items() if value == 2][0]
            return 2, number_to_check_if_tie

        if self.high_card(hand):
            number_to_check_if_tie = max(hand.values)
            return 1, number_to_check_if_tie

    def royal_flush(self, hand):
        return Counter(hand.values) == Counter([10, 11, 12, 13, 14]) and self.flush(hand)

    def straight_flush(self, hand):
        return self.straight(hand) and self.flush(hand)

    def four_of_a_kind(self, hand):
        return 4 in Counter(hand.values).values()

    def full_house(self, hand):
        counter_values = Counter(hand.values).values()
        return (2 in counter_values) and (3 in counter_values)

    def flush(self, hand):
        return all(x == hand.suits[0] for x in hand.suits)

    def straight(self, hand):
        sorted_values = sorted(hand.values)
        return sorted_values == list(range(min(sorted_values), (max(sorted_values)+1)))

    def three_of_a_kind(self, hand):
        return 3 in Counter(hand.values).values()

    def two_pairs(self, hand):
        return len(Counter(hand.values)) == 3
        # it works because if the hand was a triplet this code wouldn't compile

    def one_pair(self, hand):
        return 2 in Counter(hand.values).values()

    def high_card(self, hand):
        return max(hand.values)

    def handle_tie(self):
        if self.number_to_check_if_tie_player_1 > self.number_to_check_if_tie_player_2:
            self.wins_player_1 += 1
        if self.number_to_check_if_tie_player_1 == self.number_to_check_if_tie_player_2:
            self.handle_second_tie()

    def handle_second_tie(self):
        self.remove_tie_number()
        self.sort_hands()
        self.reverse_hands()
        if self.player_1_won():
            self.wins_player_1 += 1

    def remove_tie_number(self):
        self.hand_player_1.values.remove(
            self.number_to_check_if_tie_player_1)
        self.hand_player_2.values.remove(
            self.number_to_check_if_tie_player_2)

    def sort_hands(self):
        self.hand_player_1.values = sorted(self.hand_player_1.values)
        self.hand_player_2.values = sorted(self.hand_player_2.values)

    def reverse_hands(self):
        self.hand_player_1.values = reversed(self.hand_player_1.values)
        self.hand_player_2.values = reversed(self.hand_player_2.values)

    def player_1_won(self):
        for card_player_1, card_player_2 in zip(self.hand_player_1.values, self.hand_player_2.values):
            if card_player_1 > card_player_2:
                return True
            elif card_player_1 < card_player_2:
                return False


print(poker_hands().solution())
