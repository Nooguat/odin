class Card():

#methode pour initisialiser les reglès des cartes
    def __init__(self, nbCard = 108, color = 4 , value, direction):
        self.nbCard = nbCard
        self.color = color
        self.value = value
        self.direction = direction

#methode pour les différentes couleurs possibles
    def color(self):
        self.color = [red, blue, yellow, green]

#methode pour les différentes cartes possibles
    def value (self):
        self.value = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, reverse, skip, drawTwo, wild, wildDrawFour]

#methode pour la carte reverse
    def reverse(self, direction):
        self.direction = direction.reverse()

#methode pour la carte passer
    def skip(self):
        pass

#methode pour la carte +2
    def drawTwo(self):
        pass

#methode pour la carte changement
    def wild(self):
        pass

#methode pour la carte changement de couleur + 4
    def wildDrawFour (self):
        pass