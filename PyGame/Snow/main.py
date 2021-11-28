import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


class House:
    age = 40

    def __init__(self):
        self.y = 440
        self.x = 100
        self.colour = RED
        self.height = 100
        self.width = 200

    # end procedure
    def update(self):
        pass

    def draw(self):
        pygame.draw.rect(screen, self.colour, [self.x, self.y, self.height, self.width])
    # end procdure


# end class
class Snow(pygame.sprite.Sprite):

    def __init__(self, width_start, width_end, colour):
        # call sprite constructor
        super().__init__()
        # create a sprite
        self.width_start = width_start
        self.width_end = width_end
        self.width = random.randint(self.width_start, self.width_end)
        self.image = pygame.Surface([self.width, self.width])
        self.image.fill(colour)
        # set position
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, 680)
        self.rect.y = random.randrange(0, 400)
        self.speed = 2 + (self.width*0.1)**2

    def update(self):
        self.rect.y = self.rect.y + self.speed
        if self.rect.y >= 500:
            self.rect.x = random.randrange(0, 680)
            self.rect.y = 0
            self.width = random.randint(self.width_start, self.width_end)
            self.speed = 2 + (self.width*0.1)**2


# end class
pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False
house = House()
snow_group = pygame.sprite.Group()
num_snow = 50
for i in range(0, num_snow):
    snow_group.add(Snow(7, 15, WHITE))
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here
    snow_group.update()
    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)

    # --- Drawing code should go here
    house.draw()
    snow_group.draw(screen)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
