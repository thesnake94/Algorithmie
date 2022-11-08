import random

class Game:
    def __init__(self):
        self.parties = int(input("Combien de manche voulez vous jouer ? : \n"))
        self.p1 = player(input("Entrez votre pseudo (premier joueur ou bot pour bot) : \n"))
        self.p2 = player(input("Entrez votre pseudo (deuxième joueur ou bot pour bot) : \n"))
        self.possibilites = self.p1.possibilites
        print(f"Vous allez jouer au jeu : pierre, feuille, ciseaux. Vous allez jouer en {self.parties} points gagnant. \n")
        
    def manche(self):
        j1 = self.p1.play()
        j2 = self.p2.play()
        winner = self.gagnant(j1, j2)
        if winner == "égalité":
            print("c'est un match nul \n")
        else: winner.gagne()

    def score_display(self):
        self.p1.score()
        self.p2.score()
        

    def gagnant(self, jeu1, jeu2):
        return["égalité", self.p1, self.p2][self.possibilites.index(jeu1)-self.possibilites.index(jeu2)%3]

    def start(self):
        while self.p1.point < self.parties and self.p2.point < self.parties:
            self.manche()
            self.score_display()
        
class player:
    def __init__(self, name):
        self.name = name
        self.point = 0
        self.possibilites = ["pierre", "feuille", "ciseaux"]
 
    def score(self):
        print("Le joueur " +self.name + " possède un score de " + str(self.point)+" points\n")
    
    def gagne(self):
        self.point+=1
        if self.name == "bot":
            print("Le " + self.name + " a gagné cette partie !\n")
        else :
            print("Le joueur " + self.name + " a gagné cette partie !\n")
        
    def play(self):
        action = ""
        if self.name == "bot":
            action = random.choice(["feuille", "pierre", "ciseaux"])
            print("Le bot a joué " + action +"\n") 
        else:
            e = True
            while e:
                action = input(f"{self.name} choisissez votre coup : pierre, feuille ou ciseaux ? \n")
                if action in self.possibilites:
                    e = False
                    print("Le boss " + " a joué " + action + "\n")
                else:
                    print("Aymeric tu essaies de casser le code hein !! \n")  
                
        return action

            
        
a = Game()
a.start()

