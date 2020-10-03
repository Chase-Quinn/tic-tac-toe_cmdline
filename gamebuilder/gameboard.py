# The array that contains the positions available in the board, in total there are 9
pos = [' ' for x in range(9)]


# This is the function for command line tic-tac-toe board, 
# everything is for graphics minus the positions for the letters.

def createBoard(pos):
    showBoard = '''
         {pos[0]} | {pos[1]} | {pos[2]}
         ---------
         {pos[3]} | {pos[4]} | {pos[5]}
         ---------
         {pos[6]} | {pos[7]} | {pos[8]}
        '''.format(pos = pos)

    print(showBoard)

createBoard(pos)