board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6 : ' ',
         7: ' ', 8: ' ', 9: ' '}

def start():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print(""" _____ _____ _____   _____ ___  _____   _____ _____ _____ 
|_   _|_   _/  __ \ |_   _/ _ \/  __ \ |_   _|  _  |  ___|
  | |   | | | /  \/   | |/ /_\ \ /  \/   | | | | | | |__  
  | |   | | | |       | ||  _  | |       | | | | | |  __| 
  | |  _| |_| \__/\   | || | | | \__/\   | | \ \_/ / |___ 
  \_/  \___/ \____/   \_/\_| |_/\____/   \_/  \___/\____/ 
                                                          
                                                         """)
    print("Menu :")
    print("Joueur contre Joueur (1)")
    print("Quitter (5)")
    choix = input("Choissisez parmi le menu : ")
    return(choix)

def display_grid(board):
    i = 0
    j = 0
    print("—————--------------")
    print(f"|  {board[1]}  |  {board[2]}  |  {board[3]}  |")
    print("—————--------------")
    print(f"|  {board[4]}  |  {board[5]}  |  {board[6]}  |")
    print("—————--------------")
    print(f"|  {board[7]}  |  {board[8]}  |  {board[9]}  |")
    print("—————--------------")


def fill(coord, board, joueur):
    bool = True
    if board[coord] == ' ':
        if joueur == 1:
            board[coord] = 'x'
        else:
            board[coord] = 'o'
    else:
        print("Case déjà remplie !!")
        bool = False

    return(bool)

def check(board):
    result = 0
    n = 0
    i = 1
    j = 4
    k = 7
    while n < 3:
        if board[i] + board[j] + board[k] == "ooo":
            result = 2
        elif board[i] + board[j] + board[k] == "xxx":
            result = 1
        n += 1
        i += 1
        j += 1
        k += 1
    n = 0
    i = 1
    j = 2
    k = 3
    while n < 3:
        if board[i] + board[j] + board[k] == "ooo":
            result = 2
        elif board[i] + board[j] + board[k] == "xxx":
            result = 1
        n += 3
        i += 3
        j += 3
        k += 3
    if (board[1] + board[5] + board[9] == "ooo") or (board[3] + board[5] + board[7] == "ooo"):
        result = 2
    elif (board[1] + board[5] + board[9] == "xxx") or (board[3] + board[5] + board[7] == "xxx"):
        result = 1
    i = 1
    while board[i] != ' ':
        i+=1
    if i == 9:
        result = 3
    return(result)

def end(board):
    if check(board) == 1:
        print("--------------------")
        print("les croix on gagnés")
        print("--------------------")
    elif check(board) == 2:
        print("--------------------")
        print("les ronds ont gagnés")
        print("--------------------")
    elif check(board) == 3:
        print("--------------------")
        print("      Egalité       ")
        print("--------------------")

def jeu():
    if int(start()) == 1:
        joueur = 1
        display_grid(board)
        tours = 0
        while check(board) == 0:
            if joueur == 1:
                print("----------------------------------------------------------------------------------------------")
                coord = int(input("Tour du joueur 1 choissisez une case a remplir de 1 (en haut a gauche) à 8 (en bas a droite) : "))
                print("----------------------------------------------------------------------------------------------")
                if fill(coord, board, joueur) == False:
                    joueur = 1
                else:
                    joueur = 2
            else:
                print("----------------------------------------------------------------------------------------------")
                coord = int(input("Tour du joueur 2 choissisez une case a remplir de 1 (en haut a gauche) à 9 (en bas a droite) : "))
                print("----------------------------------------------------------------------------------------------")
                if fill(coord, board, joueur) == False:
                    joueur = 2
                else:
                    joueur = 1
            tours += 1
            if tours == 9:
                print("-------")
                print("Egalité")
                print("-------")
                break
            check(board)
            display_grid(board)
            end(board)
    
jeu()