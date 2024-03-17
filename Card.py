
class Card:
    def __init__(self, value, color):
        self.value = value
        self.color = color
        self.number = self.__value_to_number(value)

    def __value_to_number(self, value):
        match value:
            case 1:
                return "Ace"
            case 11:
                return "Joker"
            case 12:
                return "Queen"
            case 13:
                return "King"
            case _:
                return str(value)

    def show(self):
        return {
            'value': self.number,
            'color': self.color
        }

    def __str__(self):
        return f"{self.number} of {self.color}"