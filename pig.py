import random

class Die:
    def __init__(self):
        self.seed_random()

    def seed_random(self):
        random.seed(0)

    def roll(self):
        return random.randint(1, 6)


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def roll_die(self, die):
        return die.roll()

    def hold(self, turn_total):
        self.score += turn_total


class Game:
    def __init__(self):
        self.players = [Player("Player 1"), Player("Player 2")]
        self.die = Die()
        self.current_player_index = 0

    def switch_player(self):
        self.current_player_index = (self.current_player_index + 1) % 2

    def play(self):
        while all(player.score < 100 for player in self.players):
            current_player = self.players[self.current_player_index]
            turn_total = 0
            print(f"\n{current_player.name}'s turn:")
            
            while True:
                roll = current_player.roll_die(self.die)
                print(f"Rolled: {roll}")
                
                if roll == 1:
                    print("Rolled a 1! No points for this turn.")
                    turn_total = 0
                    self.switch_player()
                    break
                
                turn_total += roll
                print(f"Current turn total: {turn_total}, Total score: {current_player.score}")

                action = input("Type 'r' to roll again or 'h' to hold: ").lower()
                if action == 'h':
                    current_player.hold(turn_total)
                    print(f"{current_player.name} holds. Total score: {current_player.score}")
                    self.switch_player()
                    break

        winner = max(self.players, key=lambda player: player.score)
        print(f"\n{winner.name} wins with a score of {winner.score}!")


if __name__ == "__main__":
    game = Game()
    game.play()