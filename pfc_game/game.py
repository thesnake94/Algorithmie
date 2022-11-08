from player import player
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
