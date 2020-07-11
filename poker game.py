SEQUENCE = ['2', '3', '4', '5', '6', '7', '8', '9', '10',
            'J', 'Q', 'K', 'A']

VALUES = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
          '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

#A, K, Q, J, 10, all with the same suit.
def is_royal_flush(hand, suits, faces):
    if len(list(set(suits))) != 1:
        return False
    return faces == ['10', 'A', 'J', 'K', 'Q']

#Five cards in sequence, all with the same suit.
def is_straight_flush(hand, suits, faces):
    #check they are in the same suits
    if len(list(set(suits))) != 1:
        return False
    #chekc they are consecutive 5 cards in order
    if len(list(set(faces))) != 5:
        return False
    #when it is
    values = [VALUES[f] for f in faces]
    #if there is no A:
    if 'A' not in faces:
        max_value, min_value = max(values), min(values)
        #check that they are in ascending order
        return sorted(values) == list(range(min_value, max_value + 1))
    else:
        #if there is A
        values.remove(14)
        return sorted(values) in [[2, 3, 4, 5], [10, 11, 12, 13]]

#Four cards of the same rank.
def is_four_of_a_kind(hand, suits, faces):
    #to check their faces are the same not minding the suits
    for face in faces:
        if faces.count(face) == 4:
            return True
    return False

#Three of a Kind with a Pair.   
def is_full_house(hand, suits, faces):
    counts = {face: faces.count(face) for face in faces}
    return sorted(list(counts.values())) == [2, 3]

# Any five cards of the same suit, not in sequence.
def is_flush(hand, suits, faces):
    #to check the cards' suits are the same (only 1 exists)
    return len(list(set(suits))) == 1

# Five cards in a sequence, but not of the same suit.
def is_straight(hand, suits, faces):
    #to check they have five cards in sequence
    if len(list(set(faces))) != 5:
        return False
    values = [VALUES[f] for f in faces]
    if 'A' not in faces:
        max_value, min_value = max(values), min(values)
        if sorted(values) == list(range(min_value, max_value + 1)):
            return True
    else:
        values.remove(14)
        if sorted(values) in [[2, 3, 4, 5], [10, 11, 12, 13]]:
            return True                             
    return False

#Three cards of the same rank.
def is_three_of_a_kind(hand, suits, faces):
    for face in faces:
        #check 3 cards (values) are the same
        if faces.count(face) == 3:
            return True
    return False

#Two different Pair.
def is_two_pairs(hand, suits, faces):
    counts = {face: faces.count(face) for face in faces}
    counts = list(counts.values())
    return counts.count(2) == 2

#Two cards of the same rank.
def is_one_pair(hand, suits, faces):
    counts = {face: faces.count(face) for face in faces}
    return 2 in counts.values()



#user input starts
def poker_hand_ranking(deck):
    hand = deck
    suits = sorted([card[-1] for card in hand])
    faces = sorted([card[:-1] for card in hand])
    if is_royal_flush(hand, suits, faces):
        return "You have a Royal Flush"
    elif is_straight_flush(hand, suits, faces):
         return "You have a Straight Flush"
    elif is_four_of_a_kind(hand, suits, faces):
        return "You have four of a Kind"
    elif is_full_house(hand, suits, faces):
        return "You have a full House"
    elif is_flush(hand, suits, faces):
        return "You have a flush"
    elif is_straight(hand, suits, faces):
        return "You have a straight"
    elif is_three_of_a_kind(hand, suits, faces):
        return "You have a three of a Kind"
    elif is_two_pairs(hand, suits, faces):
        return "You have a two Pair"
    elif is_one_pair(hand, suits, faces):
        return "You have a pair"
    else:
        #if none of these counts:
        return "High Card"
