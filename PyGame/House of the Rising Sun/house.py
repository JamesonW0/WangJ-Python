### SRC - Great code

import pygame
import time

# Colours
white = (255, 255, 255)
dark_blue = (20, 12, 236)
light_blue = (12, 161, 236)
yellow = (255, 255, 0)
brown = (135, 62, 35)

# Initiate
pygame.init()
# Blank screen
size = (640, 480)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('House')  # Set title
done = False  # Exit pygame flag set to false
sun_x = 0
sun_y = 60
start = 0
end = 0
clock = pygame.time.Clock()  # Manage how fast the screen refreshes
image = pygame.image.load(r'img_house.PNG')  # load image
image = pygame.transform.scale(image, (200, 150))  # image resize

# Main
while not done:
    # User input and control
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        # End if
    # Next event
    if sun_x < 710:
        screen.fill(light_blue)
        # Sun running
        pygame.draw.circle(screen, yellow, (sun_x, sun_y), 40, 0)
        sun_x += 1
        sun_y = int(round((sun_x ** 2) * (9 / 5120) - (9 / 8) * sun_x + 240, 0))
    else:
        screen.fill(dark_blue)
        if start == 0:
            start = time.time()
        # End if
        end = time.time()
        if (end - start) > 3:
            sun_x = 0
            start = 0
        # End if
    # End if
    #screen.blit(image, (220, 165))  # House
    pygame.display.flip()  # flip the display
    clock.tick(180)  # tick the clock over
# End while

pygame.quit()
