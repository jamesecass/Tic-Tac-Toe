from colorama import Fore, Style
board = [["-" for _ in range(3)]for _ in range(3)]
def draw_board():
    for i in range(3):
        print(" ".join(board[i]))

def player_input(player):
    x , y = float("inf") , float("inf")
    while  -1 >= x or x > 3:
        try: x = int(input(f"Enter x coord (1 - 3) player {player}: ")) - 1
        except ValueError: print("Try again")
    while  -1 >= y or y > 3:
        try: y = int(input(f"Enter y coord (1 - 3) Player {player}: ")) - 1
        except ValueError: print("Try again")
    return x , y

def check_winner():
    for row in range(len(board)): 
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] != "-": return True
    for col in range(len(board[0])): 
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != "-": return True
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "-": return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "-": return True
    else: return False

def check_draw():
    for j in range(len(board)):
        if "-" in board[j]:
            return False
    return "Draw"

def main():
    player = X = Fore.RED + "X" + Style.RESET_ALL
    while check_winner() == check_draw():
        draw_board()
        x, y = player_input(player)
        if board[y][x] == "-":
            board[y][x] = player
            player = Fore.BLUE + "O" + Style.RESET_ALL if player == Fore.RED + "X" + Style.RESET_ALL else Fore.RED + "X" + Style.RESET_ALL
        else:
            print("That spot is already taken! Try again.")
    draw_board()
    if check_winner():
        player = Fore.BLUE + "O" + Style.RESET_ALL if player == Fore.RED + "X" + Style.RESET_ALL else Fore.RED + "X" + Style.RESET_ALL
        print(f"Player {player} Won")
    else: 
        print(check_draw())

if __name__ == "__main__":
    main()
