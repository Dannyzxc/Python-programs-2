TheBoard = {
    'tl': '', 'tm': '', 'tr': '',
    'ml': '', 'mm': '', 'mr': '',
    'bl': '', 'bm': '', 'br': '',
}

def printBoard(board):
    print(board['tl']+' | '+board['tm']+' | '+board['tr'])
    print('- + - + -')
    print(board['ml'] + ' | ' + board['mm'] + ' | ' + board['mr'])
    print('- + - + -')
    print(board['bl'] + ' | ' + board['bm'] + ' | ' + board['br'])

turn ="x"
for i in range(9):
    printBoard(TheBoard)
    print('turn for ' + turn + '.which space you want to move')
    move = input()
    TheBoard[move] = turn
    if turn == 'x':
        turn = "o"
    else:
        turn = "x"
printBoard(TheBoard)


