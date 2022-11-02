# Intro to PyGame https://realpython.com/pygame-a-primer/
# https://www.pygame.org/docs/
import pygame
import sys
from pygame.locals import *
# https://docs.python.org/3/library/hashlib.html
import hashlib
# https://pandas.pydata.org/docs/
import pandas as pd
# https://docs.python.org/3/library/csv.html
import csv
# https://docs.python.org/3/library/random.html?highlight=random#module-random
import random

#  ------------------------------------------

# Anzahl der Bilder pro Sekunde
# Ändern, um die Spielgeschwindigkeit zu ändern
fps = 200

# Globale Variablen
spielfeldBreite = 500  # auf replit: 500 (800)
spielfeldHoehe = 380  # auf replit: 380 (380)
linienstaerke = 20
schlaegerGroesse = 100
schlaegerAbstand = 40

# Farbeinstellungen
schwarz = None
weiss = None

# https://www.datacamp.com/community/tutorials/role-underscore-python


def generiereFarbe():
    farbe = []
    for _ in range(0, 3):
        farbe.append(random.randint(0, 255))
    return tuple(farbe)


grenzFarbe = generiereFarbe()
spielfeldFarbe = generiereFarbe()

# Spielffeld zeichnen, auf dem gespielt wird


def zeichneSpielfeld():
    pass

# Schläger zeichnen


def zeichneSchlaeger(schlaeger):
    pass

# Ball zeichnen


def zeichneBall(ball):
    pass

# Bewegt den Ball und gibt neue Position des Balls zurück


def bewegeBall(ball, ballrichtungX, ballrichtungY):
    pass

# Überprüft, ob der Ball die Wand getroffen hat und lässt den Ball wieder abprallen.
# Gibt neue Ballrichtung zurück


def pruefeKollisionWand(ball, ballrichtungX, ballrichtungY):
    if ball.top == (linienstaerke) or ball.bottom == (spielfeldHoehe - linienstaerke):
        ballrichtungY = ballrichtungY * -1
    if ball.left == (linienstaerke) or ball.right == (spielfeldBreite - linienstaerke):
        ballrichtungX = ballrichtungX * -1
    return ballrichtungX, ballrichtungY

# Überprüft, ob der Ball den Schläger getroffen hat und lässt den Ball wieder vom Schläger abprallen


def pruefeKollisionSchlaeger(ball, schlaeger1, schlaeger2, ballrichtungX):
    if ballrichtungX == -1 and schlaeger1.right == ball.left and schlaeger1.top < ball.top and schlaeger1.bottom > ball.bottom:
        return -1
    elif ballrichtungX == 1 and schlaeger2.left == ball.right and schlaeger2.top < ball.top and schlaeger2.bottom > ball.bottom:
        return -1
    else:
        return 1

# Prüft, ob ein neuer Spielpunkt gemacht wurde und gibt den neuen score zurück


def pruefeSpielstand(schlaeger1, ball, score, ballrichtungX):
    # score zurücksetzen falls linker Spielfeldrand getroffen wurde
    if ball.left == linienstaerke:
        schreibeHighscore(name, score)
        return 0
    # 1 Punkt beim Treffen des Balls zum Spielstand addieren
    elif ballrichtungX == -1 and schlaeger1.right == ball.left and schlaeger1.top < ball.top and schlaeger1.bottom > ball.bottom:
        score += 1
        return score
    # 5 Punkte für das Besiegen des Gegners addieren
    elif ball.right == spielfeldBreite - linienstaerke:
        score += 5
        return score
    # Wenn kein Spielpunkt erzielt wurde, score unverändert zurückgeben
    else:
        return score

# Künstliche Intelligenz des Computerspielers


def computerGegner(ball, ballrichtungX, schlaeger2):
    pass

# Spielstandanzeige


def zeigeSpielstand(name, score):
    resultSurf = font.render('%s: %s' % (name, score), True, weiss)
    resultRect = resultSurf.get_rect()
    resultRect.topleft = (50, 25)
    display.blit(resultSurf, resultRect)


def checkeDatei(name):
    try:
        open(name, "r")
        return True
    except IOError:
        return False


def leseHighscore(dateiName='score.csv'):
    pass


def schreibeHighscore(name, eintrag, dateiName="score.csv"):
    pass


def bekommeName(dateiName="names.txt"):
    pass


def zeichneHighscore():
    x, n, maximaleWerte, pause = 15, 0, 5, True
    # "pause" loop
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_h:
                    pause = not pause
        # highscore hintergrund zeichnen
        pygame.draw.rect(
            display,
            weiss,
            ((spielfeldBreite//4, spielfeldHoehe//4),
             (spielfeldBreite//2, spielfeldHoehe//2)),
            0)
        # highscore überschrift zeichnen
        resultSurf = font.render('BESTENLISTE', True, schwarz)
        resultRect = resultSurf.get_rect()
        resultRect.center = (spielfeldBreite // 2, 120)
        display.blit(resultSurf, resultRect)
        # highscore elemente zeichnen
        for element in leseHighscore():
            if n < maximaleWerte:
                resultSurf = font.render(' '.join(element), True, schwarz)
                resultRect = resultSurf.get_rect()
                resultRect.center = (spielfeldBreite // 2,
                                     (spielfeldHoehe // 2 - 40)+x)
                display.blit(resultSurf, resultRect)
                n, x = n + 1, x + 20
                pygame.display.update()

# https://www.programiz.com/python-programming/global-keyword


def main():
    pygame.init()

    global display, font, fontGroesse, name

    fontGroesse = 20
    font = pygame.font.Font('freesansbold.ttf', fontGroesse)
    clock = pygame.time.Clock()
    display = pygame.display.set_mode((spielfeldBreite, spielfeldHoehe))
    pygame.display.set_caption('DSCB130 - Pong')

    name = bekommeName()

    # Variablen initialisieren und Startposition setzen
    # Alle zukünftigen Änderungen der Rechtecke
    ballX = spielfeldBreite//2 - linienstaerke//2
    ballY = spielfeldHoehe//2 - linienstaerke//2
    spielerEinsPosition = (spielfeldHoehe - schlaegerGroesse) // 2
    spielerZweiPosition = (spielfeldHoehe - schlaegerGroesse) // 2
    score = 0

    # Ballrichtung
    ballrichtungX = -1  # -1 = links 1 = rechts
    ballrichtungY = -1  # -1 = hoch 1 = runter

    # Rechtecke für Ball und Schläger zeichnen
    schlaeger1 = pygame.Rect(
        schlaegerAbstand, spielerEinsPosition, linienstaerke, schlaegerGroesse)
    schlaeger2 = pygame.Rect(spielfeldBreite - schlaegerAbstand -
                             linienstaerke, spielerZweiPosition, linienstaerke, schlaegerGroesse)
    ball = pygame.Rect(ballX, ballY, linienstaerke, linienstaerke)

    # Startzustand auf dem Spielfeld zeichnen
    zeichneSpielfeld()
    zeichneSchlaeger(schlaeger1)
    zeichneSchlaeger(schlaeger2)
    zeichneBall(ball)

    pygame.mouse.set_visible(0)  # Cursor unsichtbar machen
    while True:  # Spielschleife
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # Mausbewegung -> Schläger
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
                schlaeger1.y = mousey
            # Drücke "h" wie Highscore um den highscore anzuzeigen
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_h:
                    zeichneHighscore()

        zeichneSpielfeld()
        zeichneSchlaeger(schlaeger1)
        zeichneSchlaeger(schlaeger2)
        zeichneBall(ball)

        zeigeSpielstand(name, score)

        ball = bewegeBall(ball, ballrichtungX, ballrichtungY)
        ballrichtungX, ballrichtungY = pruefeKollisionWand(
            ball, ballrichtungX, ballrichtungY)
        score = pruefeSpielstand(schlaeger1, ball, score, ballrichtungX)
        ballrichtungX = ballrichtungX * \
            pruefeKollisionSchlaeger(
                ball, schlaeger1, schlaeger2, ballrichtungX)
        schlaeger2 = computerGegner(ball, ballrichtungX, schlaeger2)

        pygame.display.update()
        clock.tick(fps)


main()
