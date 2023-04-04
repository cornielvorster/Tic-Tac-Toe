table =[
        ['','',''],
        ['','',''],
        ['','','']
    ]

def clearOutput():
    global table
    table =[
        ['','',''],
        ['','',''],
        ['','','']
    ]


def userSelection():
    x = int(input('Select the row: '))
    y = int(input('Select the column: '))

    return x, y



def placingCharacter(x, y, character):
    y= y-1
    match x:
        case 1:
            table[0][y] = character
        case 2:
            table[1][y] = character
        case 3:
            table[2][y] = character

    for i in range(0,3):
        print(table[i])


def checkHorizontalWinner():
    blank = ''
    character = ''
    win = True
    for i in range(0,3):
            if not table[i][0] == '':
                if table[i][0] == table[i][1]:
                    if table[i][0] == table[i][2]:
                        win = True
                        character = table[i][0]
                    else:
                        win = False
                
                else:
                    win = False
            else:
                pass

    if win:
         return True, character
    else:
         return False, blank
    

def checkVerticalWinner():
    blank = ''
    character = ''
    win = True
    for i in range(0,3):
            if not table[0][i] == '':
                if table[0][i] == table[1][i]:
                    if table[0][i] == table[2][i]:
                        win = True
                        character = table[0][i]
                    else:
                        win = False
                
                else:
                    win = False

    if win:
         return True, character
    else:
         return False, blank


def checkDigWinner():
    Character =''
    if table[1][1] == 'o' or table[1][1] == 'x':
        if table[0][0] == table[1][1] == table[2][2]:
            Character =table[1][1]
            return True, Character
        elif table[2][0] == table[1][1] == table[0][2]:
            Character = table[1][1]
            return True, Character
        else:
            return False, Character
    
def checkWinnerGame():
    blank = ''
    won, character = checkHorizontalWinner()
    if won == True:
        return character
    won, character = checkVerticalWinner()
    if won == True:
        return character
    won, character = checkDigWinner()
    if won == True:
        return character
    else:
        return blank
    




def main():
    count = 0
    print('This Tic-Tac-Toe written by Corniel Vorster !')
    while True:
        count = count + 1
        if not count % 2 == 0:
            print('Player 1 : ')
            x, y = userSelection()
            placingCharacter(x, y, 'x')
        else:
            print('Player 2 : ')
            x, y = userSelection()
            placingCharacter(x, y, 'o')
            
        character = checkWinnerGame()
        
        if character == 'o':
            print('Player Two is the winner')
            clearOutput()
        elif character == 'x':
            print('Player One is the winner')
            clearOutput()
        else:
            pass

        


        


main()










