from Deck import Deck
from Table import *
from Player import Player
from Computer import Computer

from main import ask_taken

def play_with_computar():
    deck = Deck()
    computer = Computer("Computer")
    user = Player("User")

    table = ShanTable([computer, user], deck)
    table.start()

    print("You got:")
    for card in user.cards:
        print(card)
    user_taken = ask_taken()
    if user_taken:
        table.take(user)
    print("Now you got: ")
    for card in user.cards:
        print(card)

    input("enter...")

    computer_taken = computer.ask_taken()
    if computer_taken:
        table.take(computer)
        print("Computer take a card")

    winners = table.shot()
    for i in winners:
        print(f"{i.name} won with - ")
        for card in i.cards:
            print(card)

if __name__ == '__main__':
    play_with_computar()