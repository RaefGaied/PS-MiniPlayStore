import os
import pygame
import subprocess

pygame.init()

WIDTH = 500
HEIGHT = 500
fps = 60
timer = pygame.time.Clock()
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Menus Des Jeux')
main_menu = False
font = pygame.font.Font('freesansbold.ttf', 20)
bg = pygame.transform.scale(pygame.image.load('mini play store.png'), (300, 300))
ball = pygame.transform.scale(pygame.image.load('mini play store.png'), (150, 150))

menu_command = 0


class Button:
    def __init__(self, txt, pos):
        self.text = txt
        self.pos = pos
        self.button = pygame.rect.Rect((self.pos[0], self.pos[1]), (260, 40))

    def draw(self):
        pygame.draw.rect(screen, 'light gray', self.button, 0, 5)
        pygame.draw.rect(screen, 'dark gray', [self.pos[0], self.pos[1], 260, 40], 5, 5)
        text2 = font.render(self.text, True, 'black')
        screen.blit(text2, (self.pos[0] + 15, self.pos[1] + 7))

    def check_clicked(self):
        if self.button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            return True
        else:
            return False


def draw_menu():
    command = -1
    pygame.draw.rect(screen, 'black', [100, 100, 300, 300])
    screen.blit(bg, (100, 100))
    pygame.draw.rect(screen, 'white', [120, 120, 260, 40], 0, 5)
    pygame.draw.rect(screen, 'gray', [120, 120, 260, 40], 5, 5)
    txt = font.render('Menus des Jeux!', True, 'black')
    screen.blit(txt, (135, 127))
    # menu exit button
    menu = Button('Exit Menu', (120, 420))
    menu.draw()
    button1 = Button('Brick breaker 1vs1 v1', (120, 180))
    button1.draw()
    button2 = Button('Bricker breaker 1vs1 v2', (120, 240))
    button2.draw()
    button3 = Button('snake game v1', (120, 300))
    button3.draw()
    button4 = Button('snake gamexbuilding v2', (120, 360))
    button4.draw()
    if menu.check_clicked():
        command = 0
    if button1.check_clicked():
        command = 1
    if button2.check_clicked():
        command = 2
    if button3.check_clicked():
        command = 3
    if button4.check_clicked():
        command = 4
    return command


def draw_game():
    txt1 = font.render('Bienvenue chez notre mini play store!', True, 'black')
    screen.blit(txt1, (50, 10))
    menu_btn = Button('Main Menu', (230, 450))
    menu_btn.draw()
    menu = menu_btn.check_clicked()
    screen.blit(ball, (175, 175))
    return menu


run = True
while run:
    screen.fill('light blue')
    timer.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if main_menu:
        menu_command = draw_menu()
        if menu_command != -1:
            main_menu = False

            if menu_command == 1:
                subprocess.Popen(['python', 'brick breakerModif.py'])
            elif menu_command == 2:
                subprocess.Popen(['python', 'game.py'])
            elif menu_command == 3:
                subprocess.Popen(['python', 'sankegameModif.py'])
            elif menu_command == 4:
                subprocess.Popen(['python', 'snake .py'])
    else:
        main_menu = draw_game()
        if menu_command > 0:
            text = font.render(f'Game {menu_command} pressed!', True, 'black')
            screen.blit(text, (150, 100))

    pygame.display.flip()
    pygame.display.update()

pygame.quit()
