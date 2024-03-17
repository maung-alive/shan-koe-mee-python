class ShanTable:
    def __init__(self, players, deck):
        self.taken_players = []
        self.players = players
        self.deck = deck
        self.winners = []

    def start(self):
        self.deck.randomize()
        for i in range(2):
            for player in self.players:
                card = self.deck.pop()
                player.receive(card)

    def take(self, player):
        if player not in self.taken_players:
            card = self.deck.pop()
            player.receive(card)
            self.taken_players.append(player)
            return card
        return False

    def shot(self):
        old_player = self.players[0]
        winner = old_player

        for new_player in self.players:
            if old_player.total == new_player.total:
                if old_player.power is True and new_player.power is True and old_player is not new_player:
                    self.winners.append(old_player)
                    self.winners.append(new_player)
                elif old_player.power is True:
                    winner = old_player
                elif new_player.power is True:
                    winner = new_player
            elif old_player.total > new_player.total:
                winner = old_player
            elif new_player.total > old_player.total:
                winner = new_player

            old_player = new_player

        self.winners.append(winner)

        return self.winners

