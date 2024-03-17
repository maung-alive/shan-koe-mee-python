class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.total = 0
        self.power = False

    def __check_null(self, total):
        if total > 10:
            total = total-10

        if total > 10:
            self.__check_null(total)

        return total

    def __check_power(self):
        color = ''
        for card in self.cards:
            if card.color == color:
                self.power = True
            else:
                self.power = False
            color = card.color

    def __add_cards(self):
        i = 0
        for card in self.cards:
            if card.value in [10, 11, 12, 13]:
                i += 0
            else:
                i += card.value

        if i == 10:
            i = 0

        i = self.__check_null(i)
        self.total = i

    def receive(self, card):
        self.cards.append(card)
        self.__add_cards()
        self.__check_power()