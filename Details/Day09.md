# Tic Tac Toe Game

> **_Develop a two player Tic Tac Toe Game where users enter the columns based on the keyboard number pad layout of 1-9_**


```python
def print_board(board):
    print(board['7']+'|'+board['8']+'|'+board['9'])
    print('-+-+-')
    print(board['4']+'|'+board['5']+'|'+board['6'])
    print('-+-+-')
    print(board['1']+'|'+board['2']+'|'+board['3'])
    
def check_success(board):
    if board['7'] == board['8'] == board['9']:
        return True
    elif board['4'] == board['5'] == board['6']:
        return True
    elif board['1'] == board['2'] == board['3']:
        return True
    elif board['1'] == board['4'] == board['7']:
        return True
    elif board['2'] == board['5'] == board['8']:
        return True
    elif board['3'] == board['6'] == board['9']:
        return True
    elif board['7'] == board['5'] == board['3']:
        return True
    elif board['1'] == board['5'] == board['9']:
        return True
    else:
        return False

def get_input(board, player):
    valid = False
    while not valid:
        val = input(f'{player}, Please Enter column no which is not x or o: ')
        if val.isdigit() and val in board.keys() and board[val] not in ('x', 'o'):
            return val
                
    
    
def play_game():
    board = {'1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9'}
    x = False
    o = False
    
    for i in range(9):
        print_board(board)
        if x == False:
            v = get_input(board, 'X')
            board[v] = 'x'
            x=True
            o=False
        elif 0 == False:
            v = get_input(board, 'O')
            board[v] = 'o'
            x=False
            o=True
        win = check_success(board)
        if win:
            print_board(board)
            if x == True:
                print('X Wins!!!')
                break
            else:
                print('O Wins!!!')
                break
        else:
            continue
    
    if not win:
        print_board(board)
        print('Game ends in Draw!!')
    
play_game()            
```

    7|8|9
    -+-+-
    4|5|6
    -+-+-
    1|2|3
    X, Please Enter column no which is not x or o: 5
    7|8|9
    -+-+-
    4|x|6
    -+-+-
    1|2|3
    O, Please Enter column no which is not x or o: 1
    7|8|9
    -+-+-
    4|x|6
    -+-+-
    o|2|3
    X, Please Enter column no which is not x or o: 2
    7|8|9
    -+-+-
    4|x|6
    -+-+-
    o|x|3
    O, Please Enter column no which is not x or o: 8
    7|o|9
    -+-+-
    4|x|6
    -+-+-
    o|x|3
    X, Please Enter column no which is not x or o: 4
    7|o|9
    -+-+-
    x|x|6
    -+-+-
    o|x|3
    O, Please Enter column no which is not x or o: 6
    7|o|9
    -+-+-
    x|x|o
    -+-+-
    o|x|3
    X, Please Enter column no which is not x or o: 3
    7|o|9
    -+-+-
    x|x|o
    -+-+-
    o|x|x
    O, Please Enter column no which is not x or o: 7
    o|o|9
    -+-+-
    x|x|o
    -+-+-
    o|x|x
    X, Please Enter column no which is not x or o: 9
    o|o|x
    -+-+-
    x|x|o
    -+-+-
    o|x|x
    Game ends in Draw!!
    
