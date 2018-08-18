import pygame
import os
import gradients


class Button:

    def __init__(self, w, h, x, y, alpha, mode, canvas, placeholder, clor, error, error_alpha):
        self.w = w
        self.h = h
        self.alpha = alpha
        self.error_alpha = error_alpha
        self.x = x
        self.y = y
        self.clor = clor
        self.imutable = clor
        self.mode = mode
        self.canvas = canvas
        self.value = ""
        self.placeholder = placeholder
        self.error = error

    def render(self):
        if self.mode == 1:
            self.canvas.blit(gradients.squared(self.h, self.w // self.h, (self.clor, 255, self.clor, self.alpha),
                                               (self.clor, 255, self.clor, 255)), (self.x, self.y))
        else:
            s = pygame.Surface((self.w, self.h), pygame.SRCALPHA)  # per-pixel alpha
            s.fill(self.alpha)  # notice the alpha value in the color
            self.canvas.blit(s, (self.x, self.y))
            # pygame.draw.rect(self.canvas, self.alpha, (self.x, self.y, self.w, self.h), 1)
            if self.value == "":
                if self.alpha == self.error_alpha:
                    display_text(self.x + 20, (self.h - 20) // 2 + self.y, None, 25, self.error, (155, 155, 155),
                                 self.canvas)
                else:
                    display_text(self.x + 20, (self.h - 20) // 2 + self.y, None, 25, self.placeholder, (155, 155, 155),
                                 self.canvas)

    def activate(self, mouse_pos):
        if mouse_pos[0] <= self.x or mouse_pos[0] >= self.x + self.w or mouse_pos[1] <= self.y or \
                mouse_pos[1] >= self.y + self.h:
            if self.clor < self.imutable - 10:
                self.clor += 10
            else:
                self.clor = self.imutable
            return False
        if self.clor <= self.imutable // 3:
            self.clor = self.imutable // 3
        else:
            self.clor -= 10
        return True


class DropDown:

    def __init__(self, options, w, h, x, y, canvas, alpha, color, dr_alpha):
        self.text = options
        self.value = options[0]
        self.down = pygame.image.load(os.path.join('data', 'down.png'))
        self.up = pygame.image.load(os.path.join('data', 'up.png'))
        self.buttons = []
        for i in range(len(options)):
            temp_but = Button(w, h, x, y + (i + 1) * h, dr_alpha, 2, canvas, "", 255, "", (0, 0, 0, 0))
            self.buttons.append(temp_but)
        self.canvas = canvas
        self.main_box = Button(w, h, x, y, alpha, 2, canvas, "", 255, "", (0, 0, 0, 0))
        self.activate = False
        self.color = color

    def render(self):
        self.main_box.render()
        display_text(self.main_box.x + 20, (self.main_box.h - 20) // 2 + self.main_box.y, None, 30, self.value,
                     self.color, self.canvas)
        if self.activate:
            for i in range(len(self.buttons)):
                self.buttons[i].render()
                display_text(self.buttons[i].x + 20, (self.buttons[i].h - 20) // 2 + self.buttons[i].y, None, 30,
                             self.text[i], self.color, self.canvas)
                pygame.draw.line(self.canvas, self.main_box.alpha, (self.buttons[i].x, self.buttons[i].y),
                                 (self.buttons[i].x + self.buttons[i].w, self.buttons[i].y))
            display_image(self.up, self.main_box.x + self.main_box.w - self.main_box.h - 10,
                          self.main_box.y + 10 / 2, self.main_box.h - 10, self.main_box.h - 10, self.canvas)
        else:
            display_image(self.down, self.main_box.x + self.main_box.w - self.main_box.h - 10,
                          self.main_box.y + 10 / 2, self.main_box.h - 10, self.main_box.h - 10, self.canvas)


class SideBar:

    def __init__(self, canvas):
        self.canvas = canvas
        self.logo = pygame.image.load(os.path.join('data', 'calories-512.png'))


def display_image(img, x, y, w, h, canvas):
    img = pygame.transform.scale(img, (w, h))
    canvas.blit(img, (x, y))


def load_sound(music, loop, channel):
    pygame.mixer.Channel(channel).play(music, loop)


def display_text(x, y, _font, size, text, color, canvas):
    font = pygame.font.Font(_font, size)
    display_txt = font.render(text, True, color)
    canvas.blit(display_txt, (x, y))


def display_text_middle(_font, size, text, color, canvas, but):
    font = pygame.font.Font(_font, size)
    display_txt = font.render(text, True, color)
    canvas.blit(display_txt, ((but.w - display_txt.get_width()) // 2 + but.x,
                              (but.h - display_txt.get_height()) // 2 + but.y))


def display_text_middle_screen(width, y, _font, size, text, color, canvas):
    font = pygame.font.Font(_font, size)
    display_txt = font.render(text, True, color)
    canvas.blit(display_txt, ((width - display_txt.get_width()) // 2, y))
