#!/usr/bin/env python3

STATE = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


def read_input(player):
    position = int(input(f'Choose {player}:'))
    return position


def c(b, pos):
    if b[pos] == ' ' or b[pos] == '':
        return pos
    else:
        return b[pos]


def print_board(b):
    print("----------")
    print(f'|{c(b, 0)} |{c(b, 1)} | {c(b, 2)}|')
    print("----------")
    print(f'|{c(b, 3)} |{c(b, 4)} | {c(b, 5)}|')
    print("----------")
    print(f'|{c(b, 6)} |{c(b, 7)} | {c(b, 8)}|')
    print("----------")


def check_win(board):
    return (board[0] == board[1] and board[1] == board[2] and board[2] != ' ') or \
        (board[3] == board[4] and board[4] == board[5] and board[5] != ' ') or \
        (board[6] == board[7] and board[7] == board[8] and board[8] != ' ') or \
        (board[0] == board[3] and board[3] == board[6] and board[6] != ' ') or \
        (board[1] == board[4] and board[4] == board[7] and board[7] != ' ') or \
        (board[2] == board[5] and board[5] == board[8] and board[8] != ' ') or \
        (board[0] == board[4] and board[4] == board[8] and board[8] != ' ') or \
        (board[2] == board[4] and board[4] == board[6] and board[6] != ' ')


def main():
    moves = 0

    current_player = 'X' if moves % 2 == 0 else 'O'
    while moves <= 9 and not check_win(STATE):
        print_board(STATE)
        current_player = 'X' if moves % 2 == 0 else 'O'
        STATE[read_input(current_player)] = current_player
        moves += 1
    print_board(STATE)
    print(f'{current_player} WON')


if __name__ == '__main__':
    main()
