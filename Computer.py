from Player import Player

class Computer(Player):
    def ask_taken(self):
        total = self._Player__check_null(self.total)
        if total > 8:
            return True