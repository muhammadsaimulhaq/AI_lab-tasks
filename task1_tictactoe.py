class TicTacToe:
    def __init__(self, size=3, win_length=3):
        self.size = size
        self.win_length = win_length
        self.board = [[" " for _ in range(size)] for _ in range(size)]
        self.current_player = "X"
        self.moves_count = 0

    def print_board(self):
        print("\n  " + "   ".join(str(i) for i in range(self.size)))
        for i in range(self.size):
            row_display = []
            for j in range(self.size):
                row_display.append(self.board[i][j])
            print(f"{i} " + " | ".join(row_display))
            if i < self.size - 1:
                print("  " + "-" * (self.size * 4 - 3))

    def make_move(self, row, col):
        if 0 <= row < self.size and 0 <= col < self.size:
            if self.board[row][col] == " ":
                self.board[row][col] = self.current_player
                self.moves_count += 1
                return True
            else:
                print(" Cell already taken! Try again.")
                return False
        else:
            print(f" Invalid position! Please enter values between 0 and {self.size-1}.")
            return False

    def check_winner(self):
        # Check rows
        for i in range(self.size):
            for j in range(self.size - self.win_length + 1):
                if all(self.board[i][j+k] == self.current_player for k in range(self.win_length)):
                    return True

        # Check columns
        for j in range(self.size):
            for i in range(self.size - self.win_length + 1):
                if all(self.board[i+k][j] == self.current_player for k in range(self.win_length)):
                    return True

        # Check diagonals (top-left to bottom-right)
        for i in range(self.size - self.win_length + 1):
            for j in range(self.size - self.win_length + 1):
                if all(self.board[i+k][j+k] == self.current_player for k in range(self.win_length)):
                    return True

        # Check diagonals (top-right to bottom-left)
        for i in range(self.size - self.win_length + 1):
            for j in range(self.win_length - 1, self.size):
                if all(self.board[i+k][j-k] == self.current_player for k in range(self.win_length)):
                    return True

        return False

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def is_draw(self):
        return self.moves_count == self.size * self.size

    def get_valid_moves(self):
        moves = []
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == " ":
                    moves.append((i, j))
        return moves

    def reset_game(self):
        self.board = [[" " for _ in range(self.size)] for _ in range(self.size)]
        self.current_player = "X"
        self.moves_count = 0


def get_game_settings():
    while True:
        try:
            size = int(input("Enter board size (3 for 3x3, 15 for 15x15, etc.): "))
            if size < 3:
                print("Board size must be at least 3!")
                continue
            
            win_length = int(input(f"Enter winning line length (3 to {size}): "))
            if win_length < 3 or win_length > size:
                print(f"Winning length must be between 3 and {size}!")
                continue
                
            return size, win_length
        except ValueError:
            print("Please enter valid numbers!")


def main():
    print("=== UNIVERSAL TIC-TAC-TOE GAME ===")
    
    while True:
        size, win_length = get_game_settings()
        game = TicTacToe(size, win_length)
        
        print(f"\nStarting {size}x{size} Tic-Tac-Toe (Win with {win_length} in a line)")
        
        while True:
            game.print_board()
            print(f"\nPlayer {game.current_player}'s turn")
            print(f"Available moves: {len(game.get_valid_moves())}")
            
            try:
                r = int(input(f"Enter row (0-{size-1}): "))
                c = int(input(f"Enter column (0-{size-1}): "))
                
                if game.make_move(r, c):
                    if game.check_winner():
                        game.print_board()
                        print(f"\n🎉 Player {game.current_player} Wins! 🎉")
                        break
                    elif game.is_draw():
                        game.print_board()
                        print("\n🤝 It's a Draw! 🤝")
                        break
                    game.switch_player()
                    
            except ValueError:
                print("Please enter valid numbers!")
        
        play_again = input("\nPlay again? (y/n): ").lower()
        if play_again not in ['y', 'yes']:
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()