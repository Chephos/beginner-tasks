

board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row,col = find

    for i in range(1,10):
        if valid(bo,i,(row,col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False

    
def valid(bo:list,num:int,pos:tuple):

    # Check row
    for col in range(len(bo[0])):
        if bo[pos[0]][col] == num and pos[1]!=col:
            return False

    # Check column
    for row in range(len(bo)):
        if bo[row][pos[1]] == num and pos[0] != row:
            return False

    
    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3,box_y*3+3):
        for j in range(box_x*3,box_x*3+3):
            if bo[i][j]==num and (i,j)!=pos:
                return False

    return True


def print_board(bo):
    for r in range(len(bo)):
        if r%3==0 and r != 0:
            print('-  -  -  -  -  -  -  -  -  -  -')
        for c in range(len(bo[r])):
            if c % 3==0 and c!= 0:
                print(' | ',end='')
            if c == 8:
                print(bo[r][c])
            else:
                print(f'{bo[r][c]} ',end=' ')

def find_empty(bo):
    for row in range(len(bo)):
        for col in range(len(bo[row])):
            if bo[row][col] == 0:
                return (row,col)
    return False


print_board(board)
solve(board)
print('----------------------------------')
print_board(board)
