import random
class deck:
    def __init__(self):
        self.suit=["Club","Diamond","Heart","Spade"]
        self.rank=['1','2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']
        self.cards=[]
    def pack_of_cards(self):
        for suit in self.suit:
            for rank in self.rank:
                self.cards.append(rank + ' of ' + suit)
        return self.cards

    def shuffle_of_cards(self):
        shuffle_cards = random.sample(self.pack_of_cards(),36)
        print(f'The cards disturbuted to the four players are: {shuffle_cards}')

        shuffle_to_player1 = shuffle_cards[:9]
        shuffle_to_player2 = shuffle_cards[9:18]
        shuffle_to_player3 = shuffle_cards[18:27]
        shuffle_to_player4 = shuffle_cards[27:]

        print(f'The cards distributed to player 1 is: {shuffle_to_player1}')
        print(f'The cards distributed to player 2 is: {shuffle_to_player2}')
        print(f'The cards distributed to player 3 is: {shuffle_to_player3}')
        print(f'The cards distributed to player 4 is: {shuffle_to_player4}')

obj_of_deck = deck()
obj_of_deck.shuffle_of_cards()


