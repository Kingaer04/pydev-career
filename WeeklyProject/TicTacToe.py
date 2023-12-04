import os
from random import randint as rand


class TicTacToe:
    winner = None
    def __init__(self, currentPlayer:str='X') ->None:
        self.currentPlayer = currentPlayer

    # Print the board
    def printboard(self,board) -> None:
        print(f'\t\t\t{board[0]} | {board[1]} | {board[2]}\t\t\t')
        print('\t\t\t----------\t\t\t')
        print(f'\t\t\t{board[3]} | {board[4]} | {board[5]}\t\t\t')
        print('\t\t\t----------\t\t\t')
        print(f'\t\t\t{board[6]} | {board[7]} | {board[8]}\t\t\t')

    # Taking user input
    def userinput(self,board) -> None:
        user = int(input('Enter number 1-9: '))
        if user >= 1 and user <=9 and board[user - 1] == '-':
            board[user -1] = self.currentPlayer
            return True
        else:
            print('Invalid move!')
            return False
    # Check for wins
    def checkhorizontal(self, board):
        if board[0] == board[1] == board[2] and board[0] != '-':
            self.winner = board[0]
            return True
        elif board[3] == board[4] == board[5] and board[3] != '-':
            self.winner = board[3]
            return True
        elif board[6] == board[7] == board[8] and board[6] != '-':
            self.winner = board[6]
            return True
        
    def checkrow(self, board):
        if board[0] == board[3] == board[6] and board[0] != '-':
            self.winner = board[0]
            return True
        elif board[1] == board[4] == board[7] and board[1] != '-':
            self.winner = board[1]
            return True
        elif board[2] == board[5] == board[8] and board[2] != '-':
            self.winner = board[2]
            return True
        
    def checkdiagonal(self, board):
        if board[0] == board[4] == board[8] and board[0] != '-':
            self.winner = board[0]
            return True
        elif board[2] == board[4] == board[6] and board[2] != '-':
            self.winner = board[2]
            return True
        
    # Check for tie
    def checktie(self, board):
        if '-' not in board:
            return True

    # Switch player
    def switchplayer(self):
        if self.currentPlayer == 'X':
            self.currentPlayer = 'O'
        else:
            self.currentPlayer = 'X'

    # Check for win
    def checkwin(self):
        if  self.checkhorizontal(gameboard) == True or self.checkrow(gameboard) == True or self.checkdiagonal(gameboard) ==True:
            print(f'{self.winner} scored a point')
            return True
        return False
    
    def computer(self, board):
        if '-' in board:
            while self.currentPlayer == 'O':
                position = rand(0,8)
                if board[position] == '-':
                    board[position] = 'O'
                    self.switchplayer()
        else:
            self.switchplayer()
            

if __name__ == '__main__':    
    trial = 0
    gameboard = ['-','-','-',
                    '-','-','-',
                    '-','-','-']
    game = TicTacToe()
    player_win = {'X':0, 'O': 0}
    print("\t\t======================\t\t")
    print("\t\t=======WELCOME!=======\t\t")
    print("\t\t======================\t\t")
    user = input("1.Two player 2.Play with Bot")
    if user == '1':
        while trial < 5:
            game.printboard(gameboard)
            game.userinput(gameboard)
            game.switchplayer()
            if game.checkwin():
                player_win[game.winner] += 1
                trial += 1
                if trial == 5:
                    print('Game over!')
                    break

                os.system('clear' if os.name == 'posix' else 'cls') 
                game.printboard(gameboard)
                print(f'Player X: {player_win["X"]}')
                print(f'Player O: {player_win["O"]}')    
                print(f"Round {trial + 1}")
                gameboard = ['-'] * 9  # Reset the game board
            else:
                if game.checktie(gameboard):
                    trial += 1
                    if trial < 5:
                        os.system('clear' if os.name == 'posix' else 'cls') 
                        game.printboard(gameboard)
                        print('It\'s a tie')
                        print(f'Player X: {player_win["X"]}')
                        print(f'Player O: {player_win["O"]}')
                        print(f"Round {trial + 1}")
                        gameboard = ['-'] * 9
                    elif trial == 5:
                        print('Game Over!')
    elif user == '2':
        while trial < 5:
            game.printboard(gameboard)
            if game.currentPlayer == 'X':
                valid = game.userinput(gameboard)
                if not valid:
                    continue
            game.switchplayer()
            game.computer(gameboard)
            if game.checkwin():
                trial += 1
                if trial == 5:
                    print('Game Over!')
                    
                os.system('clear' if os.name == 'posix' else 'cls') 
                player_win[game.winner] += 1
                game.printboard(gameboard)
                print(f'Player X: {player_win["X"]}')
                print(f'Player O: {player_win["O"]}')
                print(f'Round {trial + 1}')
                gameboard = ["-"] *9
            else:
                if game.checktie(gameboard):
                    trial += 1
                
                    if trial < 5:
                        os.system('clear' if os.name == 'posix' else 'cls') 
                        game.printboard(gameboard)
                        print('It\'s a tie')
                        print(f'Player X: {player_win["X"]}')
                        print(f'Player O: {player_win["O"]}')
                        print(f"Round {trial + 1}")
                        gameboard = ['-'] * 9
                    
                if trial == 5:
                    print('Game Over!')
                    break
