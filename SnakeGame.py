import pygame
import random
pygame.init()

#fill colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

#Setting name
pygame.display.set_caption("Snake🐍 Game by Aman")


#CREATING WINDOW
width = 900
height = 600
gamewindow = pygame.display.set_mode((width, height))



clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gamewindow.blit(screen_text, [x,y])   #update screen

def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

#GAME loop
def gameloop():

    #Game specific variables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    x_velocity = 0
    y_velocity = 0
    snake_size = 15
    fps = 30            #frame per second
    food_x = random.randint(10, width/2)
    food_y = random.randint(10, height/2)
    snk_list = []
    snk_length = 1
    score = 0

    while not exit_game:

        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    x_velocity =  10
                    y_velocity = 0

                if event.key == pygame.K_DOWN:
                    y_velocity = 10
                    x_velocity = 0

                if event.key == pygame.K_LEFT:
                    x_velocity =  -10
                    y_velocity = 0

                if event.key == pygame.K_UP:
                    y_velocity = -10
                    x_velocity = 0

        if abs(snake_x - food_x) < 10 and abs(snake_y - food_y) < 10:
            score = score+1
            #print("score is", score * 10)
            snk_length +=2
            food_x = random.randint(10, width/2)
            food_y = random.randint(10, height/2)


        snake_x = snake_x + x_velocity
        snake_y = snake_y + y_velocity
        gamewindow.fill(white)
        text_screen("Score: " + str(score * 10), red, 5, 5)

        head = []
        head.append(snake_x)
        head.append(snake_y)
        snk_list.append(head)

        if len(snk_list)>snk_length:
            del snk_list[0]

        if(snake_x < 0 or snake_x>width or snake_y < 0 or snake_y > height):
            game_over = True
            #print('GameOver')
        if (game_over == True):
            gamewindow.fill(white)
            text_screen("Oops! OUT!! Press ENTER to play again!", black, 70, 270)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    gameloop()


        #pygame.draw.rect(gamewindow, black, [snake_x, snake_y, snake_size, snake_size])
        plot_snake(gamewindow, black, snk_list, snake_size)

        pygame.draw.rect(gamewindow, red, [food_x, food_y, snake_size, snake_size])
        pygame.display.update()
        clock.tick(fps)


    pygame.quit()
    quit()

gameloop()