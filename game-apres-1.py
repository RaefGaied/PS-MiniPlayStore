import pygame
import time
import random

pygame.init()

# Couleurs
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Taille de l'écran
dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Jeu de Serpent')

# Vitesse du serpent
snake_block = 10
snake_speed = 8

clock = pygame.time.Clock()

font_style = pygame.font.SysFont(None, 50)


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])
def our_snake(snake_block, snake_list, obstacles):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
    
    for obstacle in obstacles:
        pygame.draw.rect(dis, red, [obstacle[0], obstacle[1], snake_block, snake_block])

def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1
    obstacles = []  # Déplacer la déclaration des obstacles ici


    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    # Initialisation du score
    score = 0

    while not game_over:

        while game_close == True:
            dis.fill(blue)
            message("Tu as perdu ! Appuie sur C pour rejouer ou Q pour quitter", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True
        for obstacle in obstacles:
            if snake_head[0] == obstacle[0] and snake_head[1] == obstacle[1]:
             game_close = True

        our_snake(snake_block, snake_list, obstacles)  # Passer la liste des obstacles à notre fonction our_snake

        # Affichage du score
        font = pygame.font.SysFont(None, 30)
        score_display = font.render("Score: " + str(score), True, black)
        dis.blit(score_display, (10, 10))

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            length_of_snake += 1
            # Augmentation du score
            score += 10  # Par exemple, vous pouvez ajuster cela selon votre préférence
            new_obstacle = [round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0,
                    round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0]
            obstacles.append(new_obstacle)
        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
