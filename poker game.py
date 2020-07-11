SEQUENCE = ['2', '3', '4', '5', '6', '7', '8', '9', '10',
            'J', 'Q', 'K', 'A']

VALUES = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
          '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

def is_royal_flush(hand, suits, faces):
    if len(list(set(suits))) != 1:
        return False
    return faces == ['10', 'A', 'J', 'K', 'Q']

def is_straight_flush(hand, suits, faces):
    if len(list(set(suits))) != 1:
        return False
    if len(list(set(faces))) != 5:
        return False
    values = [VALUES[f] for f in faces]
    if 'A' not in faces:
        max_value, min_value = max(values), min(values)
        return sorted(values) == list(range(min_value, max_value + 1))
    else:
        values.remove(14)
        return sorted(values) in [[2, 3, 4, 5], [10, 11, 12, 13]]

def is_four_of_a_kind(hand, suits, faces):
    for face in faces:
        if faces.count(face) == 4:
            return True
    return False

def is_straight(hand, suits, faces):
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

def is_flush(hand, suits, faces):
    return len(list(set(suits))) == 1
    
def is_full_house(hand, suits, faces):
    counts = {face: faces.count(face) for face in faces}
    return sorted(list(counts.values())) == [2, 3]

def is_three_of_a_kind(hand, suits, faces):
    for face in faces:
        if faces.count(face) == 3:
            return True
    return False

def is_two_pairs(hand, suits, faces):
    counts = {face: faces.count(face) for face in faces}
    counts = list(counts.values())
    return counts.count(2) == 2

def is_one_pair(hand, suits, faces):
    counts = {face: faces.count(face) for face in faces}
    return 2 in counts.values()

def poker_hand_ranking(deck):
    hand = deck
    suits = sorted([card[-1] for card in hand])
    faces = sorted([card[:-1] for card in hand])
    if is_royal_flush(hand, suits, faces):
        return "Royal Flush"
    elif is_straight_flush(hand, suits, faces):
         return "Straight Flush"
    elif is_four_of_a_kind(hand, suits, faces):
        return "Four of a Kind"
    elif is_full_house(hand, suits, faces):
        return "Full House"
    elif is_flush(hand, suits, faces):
        return "Flush"
    elif is_straight(hand, suits, faces):
        return "Straight"
    elif is_three_of_a_kind(hand, suits, faces):
        return "Three of a Kind"
    elif is_two_pairs(hand, suits, faces):
        return "Two Pair"
    elif is_one_pair(hand, suits, faces):
        return "Pair"
    else:
        return "High Card"