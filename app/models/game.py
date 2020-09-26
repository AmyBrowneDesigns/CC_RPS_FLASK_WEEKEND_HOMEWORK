class Game():

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2



    def rps(self, Player1, Player2):
        if Player1.choice == "rock" and Player2.choice == 'paper':
            return "Paper covers rock, Player2 wins!"
        elif Player1.choice == "rock" and Player2.choice == "scissors":
            return "Rock smashes scissors, Player1 wins!"
        elif Player1.choice == 'rock' and Player2.choice == "rock":
            return "Draw!"

        elif Player1.choice == "paper" and Player2.choice == "rock":
            return "Paper covers rock, player 1 wins"
        elif Player1.choice == 'paper' and Player2.choice == 'scissors':
            return "scissors cuts paper, player 2 wins"
        elif Player1.choice == 'paper' and Player2.choice == 'paper':
            return "Draw!"
            
        elif Player1.choice == 'scissors' and Player2.choice == 'paper':
            return 'scissors cuts paper, player 1 wins'
        elif Player1.choice == 'scissors' and Player2.choice == 'rock':
            return "rock smashes scissors, player 2 wins"
        elif Player1.choice == 'scissors' and Player2.choice == 'scissors':
            return "Draw!"
