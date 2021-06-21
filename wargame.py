
from random import shuffle

suite = 'H D S C'.split()
ranks = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck:

    def __init__(self):
        print('Create ordered deck')
        self.all_cards = [(su,rank) for su in suite for rank in ranks ]
        # print(self.all_cards)

    def shuffle(self):
        shuffle(self.all_cards)
        print(self.all_cards)

    def devide_into_half(self):
        return(self.all_cards[0:26],self.all_cards[26:])

class Hand:
    def __init__(self,cards):
        self.cards =cards

    def remove_cards(self):
        return self.cards.pop()

    def add_cards(self,added_cards):
        self.cards.extend(added_cards)

class Player:
    def __init__(self,name,hand):
        self.name = name
        self.hand = hand

    def drap_cards(self):
        drap_card = self.hand.remove_cards()
        print(self.name,'get a card',drap_card)
        return drap_card

    def balance_cards(self):
        bet_cards =[]
        if len(self.hand.cards) < 3:
            return bet_cards
        else:
            for i in range(3):
                bet_cards.append(self.hand.cards.pop())

        return bet_cards

    def check_remain_cards(self):
        flag = len(self.hand.cards) !=0
        return flag

deck = Deck()
deck.shuffle()
my_cards,computer_cards = deck.devide_into_half()
print(my_cards,computer_cards)

computer = Player('My Computer',Hand(computer_cards))
mine = Player('My Turn',Hand(my_cards))

round = 0
war_count = 0

while computer.check_remain_cards() and mine.check_remain_cards():

    round = round + 1
    print(round)

    remain_card = []

    computer_card = computer.drap_cards()
    my_card = mine.drap_cards()

    remain_card.append(computer_card)
    remain_card.append(my_card)

    if computer_card[1] == my_card[1]:
        war_count = war_count +1

        remain_card.extend(computer.balance_cards())
        remain_card.extend(mine.balance_cards())

        computer_card = computer.drap_cards()
        my_card = mine.drap_cards()

        remain_card.append(computer_card)
        remain_card.append(my_card)

        if ranks.index(computer_card[1]) < ranks.index(my_card[1]):
            print(mine.name)
            mine.hand.add_cards(remain_card)
        else:
            computer.hand.add_cards(remain_card)
    
    else:

        if ranks.index(computer_card[1]) < ranks.index(my_card[1]):
            print(mine.name)
            mine.hand.add_cards(remain_card)
        else:
            print(mine.name)
            computer.hand.add_cards(remain_card)

    print('======')

print('No of Round:',round)
print('No of War:',war_count)
print(computer.hand.cards)
print(user.hand.cards)