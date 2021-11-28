### SRC - Great code
import pygame

# Colours
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
blue = (50, 50, 255)
yellow = (255, 255, 0)
red = (255, 0, 0)

# Initiate
pygame.init()
# Set title
pygame.display.set_caption('Pong')
# Blank screen
size = (640, 480)
screen = pygame.display.set_mode(size)
# ball settings
ball_width = 20
x_val = 150
y_val = 200
x_direction = 1.7
y_direction = 1.7
# paddle settings
paddle_length = 15
paddle_width = 60
paddle_x = 0
paddle_y = 60
keys = pygame.key.get_pressed()
# font setting
font = pygame.font.Font('arial.ttf', 24)
end_font = pygame.font.Font('arial.ttf', 50)
# score and lives
score = 0
life = 10
# refresh rate
clock = pygame.time.Clock()
# exit set false
done = False

# Main
while not done:
    # User input and control
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        # End if
    # Next event
    # game settings
    screen.fill(black)
    keys = pygame.key.get_pressed()
    # text setting
    score_text = font.render('score: ' + str(score), True, black, blue)
    score_rect = score_text.get_rect()
    score_rect.topleft = (533, 22)
    life_text = font.render('lives: ' + str(life), True, black, blue)
    life_rect = life_text.get_rect()
    life_rect.topleft = (533, -2)
    # text to display
    pygame.draw.rect(screen, blue, (530, 0, 110, 50))
    screen.blit(life_text, life_rect)
    screen.blit(score_text, score_rect)
    # if life gets to zero, then you lose
    if life == 0:
        end_text = end_font.render('You lose', True, red, blue)
        end_rect = end_text.get_rect()
        end_rect.center = (320, 240)
        screen.blit(end_text, end_rect)
    # if score gets to 50, then you win
    elif score == 50:
        end_text = end_font.render('You win', True, red, blue)
        end_rect = end_text.get_rect()
        end_rect.center = (320, 240)
        screen.blit(end_text, end_rect)
    # main program, where ball and paddle are set and processed
    else:
        if keys[pygame.K_UP]:  # paddle moves up
            paddle_y -= 2.5
        elif keys[pygame.K_DOWN]:  # paddle moves down
            paddle_y += 2.5
        # End if
        # when paddle gets to the edge
        if paddle_y <= 0:
            paddle_y = 0
        elif paddle_y >= 420:
            paddle_y = 420
        # End if
        # draw paddle and ball
        pygame.draw.rect(screen, green, (x_val, y_val, ball_width, ball_width))
        pygame.draw.rect(screen, white, (paddle_x, paddle_y, paddle_length, paddle_width))
        # ball moving
        x_val += x_direction
        y_val += y_direction
        # collision detect and process
        # when hit the paddle
        if 0 <= x_val <= 15 and (paddle_y + 60) >= y_val >= (paddle_y - 20):
            x_direction = -x_direction + 0.05
            x_val = 14
            score += 1  # add 1 to the score
            if y_direction < 0:
                y_direction -= 0.05
            else:
                y_direction += 0.05
            # End if
        # when miss the paddle
        elif -30 >= x_val:
            x_val = 150
            y_val = 200
            life -= 1  # deduce 1 from life
            x_direction = abs(x_direction)
            y_direction = abs(y_direction)
        # when hit other edges
        elif x_val >= 622:
            x_direction = -x_direction
        # End if
        if y_val <= 0:
            y_direction = -y_direction
        elif y_val >= 462:
            y_direction = -y_direction
        # End if
    # End if
    pygame.display.flip()  # flip the display to renew
    clock.tick(60)  # tick the clock over
# End while

pygame.quit()
