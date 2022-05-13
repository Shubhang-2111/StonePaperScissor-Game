import pygame
import random
from pygame import mixer

pygame.init()
screen = pygame.display.set_mode((800, 600))
running = True
pygame.display.set_caption("Stone Paper Scissor")
background = pygame.image.load("background.jpg")
stoneR_icon = pygame.image.load("stone R.png")
paperR_icon = pygame.image.load("paper R.png")
scissorR_icon = pygame.image.load("scissor R.png")
stoneL_icon = pygame.image.load("stone L.png")
paperL_icon = pygame.image.load("paper L.png")
scissorL_icon = pygame.image.load("scissor L.png")
compX = 500
compY = 150
userX = 50
userY = 150
user_entry = 0
r1 = 0
user_font = pygame.font.Font("Lucky Boss.ttf", 40)
score_font = pygame.font.Font("Lucky Boss.ttf", 40)
score1 = 0
score2 = 0
score1_change = 0
score2_change = 0


def comp1(x1, y1):
    screen.blit(stoneR_icon, (x1, y1))


def comp2(x1, y1):
    screen.blit(scissorR_icon, (x1, y1))


def comp3(x1, y1):
    screen.blit(paperR_icon, (x1, y1))


def randomize():
    r = random.randint(1, 3)
    return r


def stone(x2, y2):
    screen.blit(stoneL_icon, (x2, y2))


def scissor(x2, y2):
    screen.blit(scissorL_icon, (x2, y2))


def paper(x2, y2):
    screen.blit(paperL_icon, (x2, y2))


def player_score(s):
    t = score_font.render("Score : " + str(s), True, (255, 255, 255))
    screen.blit(t, (60, 500))


def comp_score(s1):
    t = score_font.render("Score : " + str(s1), True, (255, 255, 255))
    screen.blit(t, (600, 500))


def names():
    t1 = score_font.render("Player", True, (255, 255, 255))
    t2 = score_font.render("Computer", True, (255, 255, 255))
    screen.blit(t1, (100, 100))
    screen.blit(t2, (550, 100))


def winner(u, c):
    if u == 0 and c == 0:
        return 3
    if u == c:
        return 0
    if u == 1:
        if c == 3:
            return 1
        elif c == 2:
            return 2
    if u == 2:
        if c == 1:
            return 1
        elif c == 3:
            return 2
    if u == 3:
        if c == 1:
            return 2
        elif c == 2:
            return 1


def text(player):
    t = user_font.render(f"{player} wins :D !!", True, (255, 255, 255))
    screen.blit(t, (300, 50))


def text_tie():
    t = user_font.render(f"Tie :(", True, (255, 255, 255))
    screen.blit(t, (350, 50))


def start():
    t = user_font.render("START THE GAME", True, (255, 255, 255))
    screen.blit(t, (280, 50))


while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                user_entry = 1
                r1 = randomize()
            if event.key == pygame.K_s:
                user_entry = 2
                r1 = randomize()
            if event.key == pygame.K_p:
                user_entry = 3
                r1 = randomize()
            if winner(user_entry, r1) == 1:
                lost = mixer.Sound("win.wav")
                lost.play()
            if winner(user_entry, r1) == 2:
                win = mixer.Sound("tie.wav")
                win.play()
            if winner(user_entry, r1) == 0:
                tie = mixer.Sound("lost.wav")
                tie.play()
        if event.type == pygame.KEYUP:
            score1 += score1_change
            score2 += score2_change

    score1_change = 0
    score2_change = 0
    if winner(user_entry, r1) == 3:
        start()

    if winner(user_entry, r1) == 0:
        text_tie()

    if winner(user_entry, r1) == 1:
        text("Computer")
        score2_change = 1
    if winner(user_entry, r1) == 2:
        text("Player")
        score1_change = 1
    if user_entry == 1:
        stone(userX, userY)
    if user_entry == 2:
        scissor(userX, userY)
    if user_entry == 3:
        paper(userX, userY)
    if r1 == 1:
        comp1(compX, compY)
    if r1 == 2:
        comp2(compX, compY)
    if r1 == 3:
        comp3(compX, compY)
    player_score(score1)
    comp_score(score2)
    names()
    pygame.display.update()
