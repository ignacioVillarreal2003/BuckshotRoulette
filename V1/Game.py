from Bullets import generateBulletList
from Tools import textFormat
from IA import sendMessage


def saveMessage(message):
    textFormat(message)
    return message


class Game:
    def __init__(self, player, dealer, round):
        self.player = player
        self.dealer = dealer
        self.round = round
        self.context = ""

    def play(self):
        self.context = saveMessage("Comienza el juego.")
        maxRound = self.round
        while self.round > 0:
            self.dealer.life = (maxRound - self.round + 1) * 2
            self.player.life = (maxRound - self.round + 1) * 2

            self.context += saveMessage("Ronda " + str(maxRound - self.round + 1))
            self.context += saveMessage(
                "Vida de " + str(self.dealer.name) + ": " + str(self.dealer.life) + " vida de " + str(
                    self.player.name) + ": " + str(self.player.life))

            finishGame = self.playRound()
            if finishGame:
                saveMessage("PERDISTE!!!")
                break

    def playRound(self):
        finishGame = False
        while self.dealer.life > 0 and self.player.life > 0:
            bulletList, message = generateBulletList()
            self.context += saveMessage(message)
            playerTurn = True

            for currentPosition in range(len(bulletList)):
                currentBulet = bulletList[currentPosition]
                if playerTurn:
                    playerTurn, endRound, finishGame = self.playerGame(currentBulet=currentBulet)
                else:
                    playerTurn, endRound, finishGame = self.dealerGameIA(currentBulet=currentBulet)
                if endRound:
                    break
        return finishGame

    def playerGame(self, currentBulet):
        value = input("- Ingrese a quien dispara PLAYER o DEALER:  ")
        while value != "PLAYER" and value != "DEALER":
            value = input("- Ingrese nuevamente PLAYER o DEALER:  ")
        playerTurn = self.shot(currentBulet=currentBulet, decision=value, playerTurn=True)
        endRound, finishGame = self.checkLife()
        return playerTurn, endRound, finishGame

    def dealerGameIA(self, currentBulet):
        iaText = sendMessage(self.context)
        self.context = ""
        playerTurn = self.shot(currentBulet=currentBulet,decision=iaText, playerTurn=False)
        endRound, finishGame = self.checkLife()
        return playerTurn, endRound, finishGame

    def shot(self, currentBulet, decision, playerTurn):
        if currentBulet:
            self.context += saveMessage("Habia una bala.")
            if decision == "PLAYER" and playerTurn == True:
                playerTurn = True
                self.player.decreaseLife()
                self.context += saveMessage(self.player.getLifeMessage())
            elif decision == "PLAYER" and playerTurn == False:
                playerTurn = True
                self.player.decreaseLife()
                self.context += saveMessage(self.player.getLifeMessage())
            elif decision == "DEALER" and playerTurn == True:
                playerTurn = False
                self.dealer.decreaseLife()
                self.context += saveMessage(self.dealer.getLifeMessage())
            elif decision == "DEALER" and playerTurn == False:
                playerTurn = False
                self.dealer.decreaseLife()
                self.context += saveMessage(self.dealer.getLifeMessage())
        else:
            self.context += saveMessage("No habia una bala.")
            if decision == "PLAYER" and playerTurn == True:
                self.context += saveMessage("Turno de " + str(self.player.name))
                playerTurn = True
            elif decision == "PLAYER" and playerTurn == False:
                self.context += saveMessage("Turno de " + str(self.player.name))
                playerTurn = True
            elif decision == "DEALER" and playerTurn == True:
                self.context += saveMessage("Turno de " + str(self.dealer.name))
                playerTurn = False
            elif decision == "DEALER" and playerTurn == False:
                self.context += saveMessage("Turno de " + str(self.dealer.name))
                playerTurn = False
        return playerTurn

    def checkLife(self):
        if self.player.life == 0:
            self.context += saveMessage(str(self.player.name) + " perdio la ronda.")
            endRound = True
            finishGame = True
            return endRound, finishGame
        elif self.dealer.life == 0:
            self.context += saveMessage(str(self.dealer.name) + " perdio la ronda.")
            self.round -= 1
            endRound = True
            finishGame = False
            if self.round == 0:
                finishGame = True
            return endRound, finishGame
        endRound = False
        finishGame = False
        return endRound, finishGame
