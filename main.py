from Deck import Deck
from Table import *
from Player import Player

def ask_taken():
    ans = input(f"take more y/n? ")
    match ans:
        case "y" | "Y":
            return True
        case "n" | "N":
            return False
        case _:
            ask_taken()
def play():
    deck = Deck()
    mgmg = Player("Mg Mg")
    koko = Player("Ko KO")
    kk = Player("Ki Ki")
    wiwi = Player("William")
    table = ShanTable([mgmg, koko, kk, wiwi], deck)
    table.start()

    for player in table.players:
        print(f"{player.name} got : ")
        for card in player.cards:
            print(card)

        print(f"Total is : {player.total}")

        taken = ask_taken()
        if taken:
            card = table.take(player)
            print(card)
            print(f"Now, total is : {player.total}")

    winner = table.shot()
    print("They won this turn!!")
    for i in winner:
        print(i.name)



# if __name__ == '__main__':
#     play()
