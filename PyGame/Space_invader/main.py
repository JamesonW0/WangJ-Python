import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


class Invader(pygame.sprite.Sprite):

    def __init__(self, height, width, colour, x, y, speed):
        # call sprite constructor
        super().__init__()
        # create a sprite
        self.width = width
        self.image = pygame.Surface([width, height])
        self.image.fill(colour)
        # set position
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def update(self):
        self.rect.x = self.rect.x + self.speed

    def boundary(self):
        if self.rect.x <= 0 or self.rect.x >= (700 - self.width):
            return True
        return False

    def reverse(self):
        self.speed = -self.speed
        self.rect.y += 10


# end class


class Player(pygame.sprite.Sprite):

    def __init__(self, height, width, colour, x, y, speed):
        super().__init__()
        # create a sprite
        self.image = pygame.Surface([width, height])
        self.image.fill(colour)
        # set position
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.end = pygame.time.get_ticks()

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d] and keys[pygame.K_a]:
            pass
        elif keys[pygame.K_a]:  # paddle moves left
            self.rect.x -= self.speed
        elif keys[pygame.K_d]:  # paddle moves right
            self.rect.x += self.speed
        # End if
        if keys[pygame.K_SPACE]:
            if pygame.time.get_ticks() - self.end > 350:
                self.end = pygame.time.get_ticks()
                bullet_group.add(Bullet(3, 6, WHITE, self.rect.x + 10, 3.5))
        # when player gets to the edge
        if self.rect.x <= 0:
            self.rect.x = 0
        if self.rect.x >= 680:
            self.rect.x = 680


class Bullet(pygame.sprite.Sprite):

    def __init__(self, width, height, colour, x, speed):
        super().__init__()
        # create a sprite
        self.image = pygame.Surface([width, height])
        self.image.fill(colour)
        # set position
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = 470
        self.speed = speed

    def update(self):
        self.rect.y -= self.speed


pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False
player_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
invader_group = pygame.sprite.Group()
player_group.add(Player(20, 20, GREEN, 340, 470, 5))
all_sprite_group = pygame.sprite.Group()
num_invaders = 75
invaders_row = 15
x_space = 30
y_space = 30
for i in range(0, num_invaders):
    enemy = Invader(12, 12, BLUE, 50 + x_space * (i % invaders_row), 20 + y_space * (i // invaders_row), 2)
    invader_group.add(enemy)
    all_sprite_group.add(enemy)

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    # --- Game logic should go here
    counter = 0
    reverse = False
    while counter != len(invader_group) and not reverse:
        if invader_group.sprites()[counter].boundary():
            for i in invader_group:
                i.reverse()
            reverse = True
        counter += 1
    pygame.sprite.groupcollide(bullet_group, invader_group, True, True)
    invader_group.update()
    bullet_group.update()
    player_group.update()
    # --- Screen-clearing code goes here
    screen.fill(BLACK)
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.

    # --- Drawing code should go here
    invader_group.draw(screen)
    bullet_group.draw(screen)
    player_group.draw(screen)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
