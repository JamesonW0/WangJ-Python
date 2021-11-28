import pygame
import random
from pygame import gfxdraw

# Colours
black = (0, 0, 0)
white = (255, 255, 255)
blue = (50, 50, 255)
yellow = (255, 255, 0)
orange = (235, 119, 52)
p_green = (198, 235, 52)

# Initiate
pygame.init()
size = (810, 540)  # set screen size
screen = pygame.display.set_mode(size)  # blank screen
pygame.display.set_caption('Hangman')  # Set title
done = False  # Exit pygame flag set to false
clock = pygame.time.Clock()  # Manage how fast the screen refreshes


class TextBox:

    def __init__(self, x_pos, y_pos, width, height, maxsize=-1, fontsize=40):
        self.input_box = pygame.Rect(x_pos, y_pos, width, height)
        self.font = pygame.font.Font('arial.ttf', fontsize)
        self.text = ''
        self.x = x_pos
        self.y = y_pos
        self.active = True
        self.maxsize = maxsize
        self.display = True
        self.start = pygame.time.get_ticks()
        self.engage = True
    # end procedure

    def entry_detect(self, event):
        if event.type == pygame.KEYDOWN:
            if self.engage:
                if self.active:
                    if event.key == pygame.K_RETURN:
                        return_val = self.text.upper()
                        self.text = ''
                        return return_val
                    elif event.key == pygame.K_BACKSPACE:
                        self.text = self.text[:-1]
                    else:
                        if len(self.text) != self.maxsize:
                            self.text += event.unicode
                        # end if
                    # end if
                # end if
            # end if
        # end if
    # end function

    def update(self):
        # font setting
        text_surface = self.font.render(self.text, True, black)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (self.x + 11, self.y)
        # Display input
        screen.blit(text_surface, text_rect)
        pygame.draw.rect(screen, blue, self.input_box, 3)
        if self.active:
            if pygame.time.get_ticks() - self.start > 500:
                self.display = not self.display
                self.start = pygame.time.get_ticks()
            # end if
            if self.display:
                pygame.draw.rect(screen, black, (self.x + 5 + len(self.text) * 35, self.y + 3, 3, 42))
            # end if
        # end if
    # end procedure
# end class


class LetterList:

    def __init__(self, x_pos, y_pos, delta_x, delta_y, fontsize=24):
        self.available_letters = []
        for i in range(ord('A'), ord('Z') + 1):
            self.available_letters.append(chr(i))
        # next i
        self.x = x_pos
        self.y = y_pos
        self.delta_x = delta_x
        self.delta_y = delta_y
        self.font = pygame.font.Font('arial.ttf', fontsize)
    # end procedure

    def __call__(self, item):
        if item in self.available_letters:
            del self.available_letters[self.available_letters.index(item)]
            return item
        # end if
    # end function

    def update(self):
        for i in range(0, len(self.available_letters)):
            self.draw(self.available_letters[i], self.x + (self.delta_x * (i % 3)), self.y + (self.delta_y * (i // 3)))
        # next i
    # end procedure

    def draw(self, item, x, y):
        text_surface = self.font.render(item, True, black)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (x, y)
        screen.blit(text_surface, text_rect)
    # end procedure
# end class


# print word in init section, delete after use
class Word:

    def __init__(self, x_pos, y_pos, length, space, fontsize=28, file_path='dictionaries.txt'):
        self.font = pygame.font.Font('arial.ttf', fontsize)
        self.x = x_pos
        self.y = y_pos
        self.length = length
        self.space = space
        self.hang = 0
        dictionary = open(file_path)
        lines = dictionary.readlines()
        rand_num = random.randint(0, len(lines) - 1)
        self.word = lines[rand_num][:-1]
        dictionary.close()
        self.answer = ' ' * len(self.word)
        self.timer = 0
    # end procedure

    def word_process(self):
        front = len(self.word) / 2
        start = self.x - front * (self.length + self.space)
        for i in range(0, len(self.word)):
            pygame.draw.line(screen, black, (start, self.y), (start - self.length, self.y), 2)
            self.draw_text(self.answer[i], start - 25, self.y - 30)
            start = start + self.length + self.space
        # next i
    # end procedure

    def guess(self, item):
        if item is not None:
            if item in self.word or item.lower() in self.word:
                for i in range(0, len(self.word)):
                    if self.word[i].upper() == item:
                        self.answer = self.answer[:i] + self.word[i] + self.answer[i + 1:]
                    # end if
                # next i
            # end if
            else:
                self.hang += 1
            # end if
        # end if
        return self.hang
    # end function

    def draw_text(self, item, x, y):
        text_surface = self.font.render(item, True, black)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (x, y)
        screen.blit(text_surface, text_rect)
    # end procedure
# end class


class Animation:

    def __init__(self):
        self.font = pygame.font.Font('arial.ttf', 50)
        self.x_left = -551
        self.y_left = 230
        self.x_right = 860
        self.y_right = 240
        self.length = 500
        self.width = 70
        self.state = 0
    # end procedure

    def win(self):
        self.the_end()
        win_surface = self.font.render('Win', True, orange)
        win_rect = win_surface.get_rect()
        win_rect.topleft = (self.x_right+100, self.y_right+8)
        screen.blit(win_surface, win_rect)
    # end procedure

    def lose(self):
        self.the_end()
        lose_surface = self.font.render('Lose', True, orange)
        lose_rect = lose_surface.get_rect()
        lose_rect.topleft = (self.x_right+100, self.y_right+8)
        screen.blit(lose_surface, lose_rect)
    # end procedure

    def the_end(self):
        gfxdraw.box(screen, (self.x_left, self.y_left, self.length, self.width), p_green)
        gfxdraw.filled_polygon(screen, ((self.x_left + self.length, self.y_left), (self.x_left + self.length + 50, self.y_left), (self.x_left + self.length, self.y_left + 69)), p_green)
        gfxdraw.box(screen, (self.x_right, self.y_right, self.length, self.width), p_green)
        gfxdraw.filled_polygon(screen, ((self.x_right, self.y_right), (self.x_right - 50, self.y_right + 69), (self.x_right, self.y_right + 69)), p_green)
        text_surface = self.font.render('You', True, orange)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (self.x_left + 300, self.y_left + 8)
        screen.blit(text_surface, text_rect)
        if self.state == 0:
            self.x_left += 15
            self.x_right -= 15
            if self.x_left >= 0:
                self.x_left = -115
                self.x_right = 425
                self.state = 1
            # end if
        elif self.state == 1:
            self.x_left += 0.01
            self.y_left -= 0.01
            self.x_right -= 0.01
            self.y_right += 0.01
            if self.y_right >= 248:
                self.state = 2
            # end if
        # end if
    # end procedure
# end class


class HangMan:
    # All images used from wikipedia, https://en.wikipedia.org/wiki/Hangman_(game), under the terms of the
    # GNU Free Documentation License, Version 1.2 or any later version published by the Free Software Foundation; all
    # image file is licensed under the Creative Commons Attribution-Share Alike 3.0 license; with author en:User:Demi
    # and uploading user 5ko from wikipedia.No changes made to the images stored on the device, but enlargements were
    # made to make these images suit for the program.
    def __init__(self):
        self.status_0 = pygame.image.load(r'Hangman-0.png')  # load image - hang0
        self.status_0 = pygame.transform.scale(self.status_0, (450, 450))  # image resize
        self.status_1 = pygame.image.load(r'Hangman-1.png')  # load image - hang1
        self.status_1 = pygame.transform.scale(self.status_1, (450, 450))  # image resize
        self.status_2 = pygame.image.load(r'Hangman-2.png')  # load image - hang2
        self.status_2 = pygame.transform.scale(self.status_2, (450, 450))  # image resize
        self.status_3 = pygame.image.load(r'Hangman-3.png')  # load image - hang3
        self.status_3 = pygame.transform.scale(self.status_3, (450, 450))  # image resize
        self.status_4 = pygame.image.load(r'Hangman-4.png')  # load image - hang4
        self.status_4 = pygame.transform.scale(self.status_4, (450, 450))  # image resize
        self.status_5 = pygame.image.load(r'Hangman-5.png')  # load image - hang5
        self.status_5 = pygame.transform.scale(self.status_5, (450, 450))  # image resize
        self.status_6 = pygame.image.load(r'Hangman-6.png')  # load image - hang6
        self.status_6 = pygame.transform.scale(self.status_6, (450, 450))  # image resize
        self.timer = 0
    # end procedure

    def __call__(self, trial):
        if trial == 0:
            screen.blit(self.status_0, (200, 0))
        elif trial == 1:
            screen.blit(self.status_1, (200, 0))
        elif trial == 2:
            screen.blit(self.status_2, (200, 0))
        elif trial == 3:
            screen.blit(self.status_3, (200, 0))
        elif trial == 4:
            screen.blit(self.status_4, (200, 0))
        elif trial == 5:
            screen.blit(self.status_5, (200, 0))
        else:
            screen.blit(self.status_6, (200, 0))
        # end if
    # end procedure
# end class


if __name__ == '__main__':
    errors = 0
    textbox_1 = TextBox(25, 20, 48, 48, 1)
    alphabets = LetterList(13, 80, 30, 30)
    word = Word(455, 470, 40, 10)
    gallows = HangMan()
    win_state = Animation()
    while not done:
        # User input and control
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            # end if
            errors = word.guess(alphabets(textbox_1.entry_detect(event)))
        # next event
        screen.fill(white)
        textbox_1.update()
        alphabets.update()
        word.word_process()
        gallows(errors)
        if word.answer == word.word:
            win_state.win()
            textbox_1.engage = False
        elif errors == 6:
            win_state.lose()
            textbox_1.engage = False
        pygame.display.flip()  # renew the screen
        clock.tick(300)  # tick the clock over
    # End while
    pygame.quit()
# end if

print(word.word)