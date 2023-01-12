tab = [[0,0,0],[0,0,0],[0,0,0]]


def start():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("""_____ _____ _____   _____ ___  _____   _____ _____ _____ 
|_   _|_   _/  __ \ |_   _/ _ \/  __ \ |_   _|  _  |  ___|
  | |   | | | /  \/   | |/ /_\ \ /  \/   | | | | | | |__  
  | |   | | | |       | ||  _  | |       | | | | | |  __| 
  | |  _| |_| \__/\   | || | | | \__/\   | | \ \_/ / |___ 
  \_/  \___/ \____/   \_/\_| |_/\____/   \_/  \___/\____/ 
                                                          
                                                          """)
    print("Menu :")
    print("Joueur contre Joueur (1)")
    print("Joueur contre IA (2)")
    print("Scoreboard (3)")
    print("Historique (4)")
    print("Quitter (5)")
    choix = input("Choissisez parmi le menu : ")
    return(choix)


def display_grid(tab):
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    i = 0
    j = 0
    while i < 3:
        while j < 3:
            if tab[i][j] == 0:
                if j == 0:
                    print("|", end="")
                if j == 2:
                    print("   ", end="")
                    print("|")
                else:
                    print("   ", end="")
                    print("|", end="")
            elif tab[i][j] == 1:
                if j == 0:
                    print("|", end="")
                if j == 2:
                    print(" x ", end="")
                    print("|")
                else:
                    print(" x ", end="")
                    print("|", end="")
            elif tab[i][j] == 2:
                if j == 0:
                    print("|", end="")
                if j == 2:
                    print(" o ", end="")
                    print("|")
                else:
                    print(" o ", end="")
                    print("|", end="")
            j+=1
        print("—————---------")
        j=0
        i+=1

def check(tab):
    
    result = 0
    #lignes
    if tab[0][0] == 1 and tab[0][1] == 1 and tab[0][2] == 1:
            result = 1
    elif tab[0][0] == 2 and tab[0][1] == 2 and tab[0][2] == 2:
            result = 2
    elif tab[1][0] == 1 and tab[1][1] == 1 and tab[1][2] == 1:
            result = 1
    elif tab[1][0] == 2 and tab[1][1] == 2 and tab[1][2] == 2:
            result = 2
    elif tab[2][0] == 1 and tab[2][1] == 1 and tab[1][2] == 1:
            result = 1
    elif tab[2][0] == 2 and tab[2][1] == 2 and tab[1][2] == 2:
            result = 2
    #colones
    elif tab[0][0] == 1 and tab[1][0] == 1 and tab[2][0] == 1:
            result = 1
    elif tab[0][0] == 2 and tab[1][0] == 2 and tab[2][0] == 2:
            result = 2
    elif tab[0][1] ==  1 and tab[1][1] == 1 and tab[2][1] == 1:
            result = 1
    elif tab[0][1] ==  2 and tab[1][1] == 2 and tab[2][1] == 2:
            result = 2
    elif tab[0][2] == 1 and tab[1][2] == 1 and tab[2][2] == 1:
            result = 1
    elif tab[0][2] == 2 and tab[1][2] == 2 and tab[2][2] == 2:
            result = 2
    #diagonales
    elif tab[0][0] == 1 and tab[1][1] == 1 and tab[2][2] == 1:
            result = 1
    elif tab[0][0] == 2 and tab[1][1] == 2 and tab[2][2] == 2:
            result = 2
    elif tab[0][2] == 1 and tab[1][1] == 1 and tab[2][0] == 1:
            result = 1
    elif tab[0][2] == 2 and tab[1][1] == 2 and tab[2][0] == 2:
            result = 2
    else:
        result = 0
    compt = 0
    for row in tab:
        for val in row:
            if val != 0:
                compt += 1
            
    if compt == 9:        
        result = 3
    return(result)


def end(tab):
    if check(tab) == 1:
        print("les croix on gagnés")
    elif check(tab) == 2:
        print("les rond ont gagnés")
    elif check(tab) == 3:
        print("égalité")

def fill(coord, tab, joueur):
        bool = True
        if int(coord) == 0:
            if tab[0][0] == 0:
                tab[0][0] = joueur
            else:
                print("-----------------")
                print("case déjà remplie")
                print("-----------------")
                bool = False
        elif int(coord) == 1:
            if tab[0][1] == 0:
                tab[0][1] = joueur
            else:
                print("-----------------")
                print("case déjà remplie")
                print("-----------------")
                bool = False
        elif int(coord) == 2:
            if tab[0][2] == 0:
                tab[0][2] = joueur
            else:
                print("-----------------")
                print("case déjà remplie")
                print("-----------------")
                bool = False
        elif int(coord) == 3:
            if tab[1][0] == 0:
                tab[1][0] = joueur
            else:
                print("-----------------")
                print("case déjà remplie")
                print("-----------------")
                bool = False
        elif int(coord) == 4:
            if tab[1][1] == 0:
                tab[1][1] = joueur
            else:
                print("-----------------")
                print("case déjà remplie")
                print("-----------------")
                bool = False
        elif int(coord) == 5:
            if tab[1][2] == 0:
                tab[1][2] = joueur
            else:
                print("-----------------")
                print("case déjà remplie")
                print("-----------------")
                bool = False
        elif int(coord) == 6:
            if tab[2][0] == 0:
                tab[2][0] = joueur
            else:
                print("-----------------")
                print("case déjà remplie")
                print("-----------------")
                bool = False
        elif int(coord) == 7:
            if tab[2][1] == 0:
                tab[2][1] = joueur
            else:
                print("-----------------")
                print("case déjà remplie")
                print("-----------------")
                bool = False
        elif int(coord) == 8:
            if tab[2][2] == 0:
                tab[2][2] = joueur
            else:
                print("-----------------")
                print("case déjà remplie")
                print("-----------------")
                bool = False
        return(bool)
    


def jeu():
    if int(start()) == 1:
        joueur = 1
        display_grid(tab)
        while check(tab) == 0:
            if joueur == 1:
                print("----------------------------------------------------------------------------------------------")
                coord = input("Tour du joueur 1 choissisez une case a remplir de 0 (en haut a gauche) à 8 (en bas a droite) : ")
                print("----------------------------------------------------------------------------------------------")
                if fill(coord, tab, joueur) == False:
                    joueur = 1
                else:
                    joueur = 2
                display_grid(tab)
                check(tab)
                end(tab)
            else:
                print("----------------------------------------------------------------------------------------------")
                coord = input("Tour du joueur 2 choissisez une case a remplir de 0 (en haut a gauche) à 8 (en bas a droite) : ")
                print("----------------------------------------------------------------------------------------------")
                if fill(coord, tab, joueur) == False:
                    joueur = 2
                else:
                    joueur = 1
                display_grid(tab)
                check(tab)
                end(tab)
    print("-------------------")
    choix = input("Rejouer ?? oui/non ")
    print("-------------------")
    if choix == "oui":
        jeu()            
jeu()
