import pygame

# Colours
black = (0, 0, 0)
white = (255, 255, 255)
blue = (50, 50, 255)
yellow = (255, 255, 0)

# Initiate
pygame.init()
# Blank screen
size = (640, 480)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Test')  # Set title
done = False  # Exit pygame flag set to false
clock = pygame.time.Clock()  # Manage how fast the screen refreshes

###
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
    # Drawing here
    pygame.draw.rect(screen, blue, (1, 1, 200, 150))
    pygame.draw.circle(screen, yellow, (200, 165), 40, 0)
    pygame.display.flip()  # flip the display to renew
    clock.tick(60)  # tick the clock over
# End while

pygame.quit()