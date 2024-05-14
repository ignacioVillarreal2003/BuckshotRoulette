import random


class Player:
    def __init__(self, name, maxLife):
        self.name = name
        self.life = maxLife
        self.maxLife = maxLife

    def decreaseLife(self):
        if self.life - 1 >= 0:
            self.life -= 1
        return self.life

    def getLifeMessage(self):
        return str(self.name) + " tiene " + str(self.life) + " de vida."

    def doubleOrNothing(self):
        n = random.randint(1, 2)
        if n == 1:
            self.life += 2
            if self.life > self.maxLife:
                self.life = self.maxLife
        else:
            if self.life - 1 >= 0:
                self.life -= 1
