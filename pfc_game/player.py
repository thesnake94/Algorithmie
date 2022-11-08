import random

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
