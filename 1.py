from random import randint
random_first = randint(0,1)
rows, cols = (3, 3)
map = [[' ' for i in range(cols)] for j in range(rows)]
def user_input():
    while(1):
        COORD = input().strip('(').strip(')').split(',')
        x = int(COORD[0].strip())
        y = int(COORD[1].strip())
        type(x)
        if x>=0 and x<=2 and y>=0 and y<=2:
            if map[x][y] != ' ':
                print('Already Chosen!')
                
            else:
                break
        else:
            print('Wrong Input')
    return x,y   
    # print(map)
def computer_input():
    while(1):
        x = randint(0,2)
        y = randint(0,2)
        if map[x][y] != ' ':
            continue
        else:
            break
    return x,y
def end_check(x,y,figure):
    map[x][y] = figure
    print(map)
    check = 0
    same_row = 1
    same_col = 1
    same_diag = 1
    for i in range(1,3):
       
        if x-i >=0:
            if map[x-i][y] == figure:
                same_row += 1
        if x+i <=2:
            if map[x+i][y] == figure:
                same_row += 1
        if y-i >=0:
            if map[x][y-i] == figure:
                same_col +=1
        if y+i <=2:
            if map[x][y+i] == figure:
                same_col += 1
        if x-i >=0 and y-i >=0:
            if map[x-i][y-i] == figure:
                same_diag += 1
        if x+i <=2 and y+i <=2:
            if map [x+i][y+i] == figure:
                same_diag += 1
        if same_row == 3 or same_col == 3 or same_diag == 3:
            check = 1
    if check == 1:
        return 1
    else:
        return 0
def playing():
    turn = 0
    if(random_first == 0):
        while(1):
            user_figure = 'X'
            computer_figure = 'O'
            print('User turn','Input should be (x, y) format')
            x, y = user_input()
            check = end_check(x,y,user_figure)
            turn+=1
            if(check == 1):
                print('win')
                break
            if(check == 0 and turn == 9):
                print('tie')
                break
            print('Computer turn')
            x, y = computer_input()
            check = end_check(x,y,computer_figure)
            turn+=1
            if(check == 1):
                print('lose')
                break
    else:
       while(1):
            user_figure = 'O'
            computer_figure = 'X'
            print('Computer turn')
            x, y = computer_input()
            check = end_check(x,y,computer_figure)
            turn+=1
            if(check == 1):
                print('lose')
                break
            if(check == 0 and turn == 9):
                print('tie')
                break
            print('User turn','(Input format : (x, y))')
            x, y = user_input()
            check = end_check(x,y,user_figure)
            turn+=1
            if(check == 1):
                print('win')
                break
playing()
