#
# Problem 54 Poker hands
#
# High Card: Highest value card.
# One Pair: Two cards of the same value.
# Two Pairs: Two different pairs.
# Three of a Kind: Three cards of the same value.
# Straight: All cards are consecutive values.
# Flush: All cards of the same suit.
# Full House: Three of a kind and a pair.
# Four of a Kind: Four cards of the same value.
# Straight Flush: All cards are consecutive values of same suit.
# Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

import sys

VALUE_MAP = {
    '1': 1,  '2': 2,  '3': 3,  '4': 4,  '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14,
    'H': 1,  'C': 2,  'S': 3,  'D': 4
}

HIGH_SCORE  = 1
ONE_PAIR    = HIGH_SCORE * 15
TWO_PAIR    = ONE_PAIR * 15
THREE_KIND  = TWO_PAIR * 15
STRAIGHT    = THREE_KIND * 15
FLUSH       = STRAIGHT * 15
FULL_HOUSE  = FLUSH * 15
FOUR_KIND   = FULL_HOUSE * 15
STRAIGHT_FLUSH = FOUR_KIND * 15
ROYAL_FLUSH = STRAIGHT_FLUSH * 15

# this is a dirty solution
def evaluate(cards):
    highCard = cards[-1][0]
    same = True
    score = 0
    for c in cards:
        if c[1] != cards[0][1]:
            same = False
            break
    if same:
        if cards[0][0] == 10:
            return ROYAL_FLUSH

        for i in range(1, len(cards)):
            if cards[i][0] - cards[i-1][0] != 1:
                return FLUSH

        return STRAIGHT_FLUSH
    else:
        for i in range(3, len(cards)):
            if cards[i][0] == cards[i - 3][0]:
                return FOUR_KIND * cards[i][0]

        if cards[0][0] == cards[2][0]:
            score = THREE_KIND * cards[2][0]
            if cards[3][0] == cards[4][0]:
                return score + ONE_PAIR * cards[3][0]
            else:
                return score

        if cards[2][0] == cards[4][0]:
            score = THREE_KIND * cards[2][0]
            if cards[0][0] == cards[1][0]:
                return score + ONE_PAIR * cards[0][0]
            else:
                return score
        
        if cards[1][0] == cards[3][0]:
            return THREE_KIND * cards[1][0]
        
        pairs = [0, ONE_PAIR, TWO_PAIR]
        index = 0
        for i in range(1, len(cards)):
            if cards[i][0] == cards[i-1][0]:
                index = index + 1
                score = score + pairs[index] * cards[i][0] 
        
        if score:
            if score > TWO_PAIR: print cards
            return score
        
        for i in range(1, len(cards)):
            if cards[i][0] - cards[i-1][0] != 1:
                return HIGH_SCORE * cards[-1][0]

        return STRAIGHT

def compare(p1, p2):
    score1 = evaluate(p1)
    score2 = evaluate(p2)
    if score1 == score2:
        print p1, p2
        for i in range(len(p1), 0, -1):
            if p1[i-1][0] != p2[i-1][0]:
                return p1[i-1][0] > p2[i-1][0]
    return score1 > score2
        
def convert(cards):
    # convert from literal to value
    return [(VALUE_MAP[c[0]],VALUE_MAP[c[1]]) for c in cards]

def p054(path):
    count = 0
    with open(path, 'r') as f:
        lines = f.readlines()
        for l in lines:
            cards = convert(l.strip().split())
            if compare(sorted(cards[:5]), sorted(cards[5:])):
                #print l.strip(), first, second
                count = count + 1
    return count
    
if __name__ == '__main__':
    print p054(sys.argv[1])