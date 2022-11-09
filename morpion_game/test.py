import random   
import os    
from helpers import draw_board

spots = {1 : '1', 2 : '2', 3 : '3', 4 : '4', 5 : '5',
         6 : '6', 7 : '7', 8 : '8', 9 : '9'}


class Game:
    def __init__(self):
        self.j1 = (input('Quel est le nom du premier joueur : \n'))
        self.j2 = (input('Quel est le nom du deuxième joueur : \n'))
        print(f'Bienvenue dans le jeu du Morpion !\n')
        self.playing = True
        self.turn = 0
        self.previous_turn = -1
        self.complete = False
    
    def _check_turn(self):
        if self.turn %2 == 0: 
            return 'X'
        else : return 'O'
    
    def game_play(self):
        while self.playing:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Bienvenue dans le jeu du Morpion ! \nLes joueurs sont : " + self.j1 + " Joueur 1 : 'O' " + " et " + self.j2 + " Joueur 2 : 'X' "+ "\n")
            draw_board(spots)
            if self.previous_turn == self.turn:
                print("Case occupée, choisissez en une autre ! \n")
            self.previous_turn = self.turn
            print("Joueur " + str((self.turn %2) +1) + " c'est votre tour, choisissez votre case ou q pour quitter \n")
            choice = input()
            if choice == "q":
                print("Vous avez quitter le jeu\n")
                break
            elif str.isdigit(choice) and int(choice) in spots:
                if not spots[int(choice)] in {'X', 'O'}:
                    self.turn +=1
                    spots[int(choice)] = self._check_turn()
            if self._win_event(spots): self.playing, self.complete = False, True
            if self.turn > 8: self.playing = False
        os.system('cls' if os.name == 'nt' else 'clear')
        draw_board(spots)
        if self.complete:
            if self._check_turn() == 'X' : print(self.j2 + " a gagné !\n")
            else : print(self.j1 + " a gagné !\n")
        else : print("Match nul ! \n")
        
        
                    
    def _win_event(self, spots):
        if (spots[1] == spots[2] == spots[3]) \
            or (spots[4] == spots[5] == spots[6]) \
            or (spots[7] == spots[8] == spots[9]) :
                return True
        elif (spots[1] == spots[4] == spots[7]) \
            or (spots[2] == spots[5] == spots[8]) \
            or (spots[3] == spots[6] == spots[9]) :
                return True
        elif (spots[1] == spots[5] == spots[9]) \
            or (spots[3] == spots[5] == spots[7]) :
                return True
        else : return False
        
a = Game()
a.game_play()
a._win_event(spots)
