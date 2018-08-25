import pygame
import os
import gradients
import cv2
import pickle
import numpy as np

from nutritionix1012 import NutritionixClient
from nutritionix import Nutritionix

NUTRITIONIX_APP_ID = "f6574712"
NUTRITIONIX_API_KEY = "a232f7cc5be24b44d07d94a6985a5810"
nix_client = NutritionixClient(application_id=NUTRITIONIX_APP_ID, api_key=NUTRITIONIX_API_KEY)
nix = Nutritionix(app_id=NUTRITIONIX_APP_ID, api_key=NUTRITIONIX_API_KEY)


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


class SearchBar:

    def __init__(self, canvas, x, y, w, h, alpha, placeholder, search_hints, dr_alpha, text_color):
        self.canvas = canvas
        self.main_input_box = Button(w, h, x, y, alpha, 2, canvas, placeholder, 255, "", (0, 0, 0, 0))
        self.buttons = []
        for button in range(len(search_hints)):
            temp_but = Button(w, h, x, y + (button + 1) * h, dr_alpha, 2, canvas, "", 255, "", (0, 0, 0, 0))
            self.buttons.append(temp_but)
        self.text_color = text_color

    def render(self):
        self.main_input_box.render()
        display_text(self.main_input_box.x + 20, (self.main_input_box.h - 20) // 2 + self.main_input_box.y, None, 30,
                     self.main_input_box.value, self.text_color, self.canvas)


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
    display_txt = get_text_parameter(_font, size, text, color)
    canvas.blit(display_txt, (x, y))


def display_text_middle(_font, size, text, color, canvas, but):
    display_txt = get_text_parameter(_font, size, text, color)
    canvas.blit(display_txt, ((but.w - display_txt.get_width()) // 2 + but.x,
                              (but.h - display_txt.get_height()) // 2 + but.y))


def display_text_middle_screen(width, y, _font, size, text, color, canvas):
    display_txt = get_text_parameter(_font, size, text, color)
    canvas.blit(display_txt, ((width - display_txt.get_width()) // 2, y))


def get_text_parameter(_font, size, text, color):
    font = pygame.font.Font(_font, size)
    display_txt = font.render(text, True, color)
    return display_txt


class CameraVideo:

    def __init__(self, frame, canvas, heights, x, true_height):
        self.canvas = canvas
        self.heights = heights
        self.x = x
        self.true_height = true_height
        height, width, layers = frame.shape
        ratio = self.heights / height
        new_w = int(width * ratio)
        self.camera = Button(new_w + 42, 70, x, (true_height + heights) // 2 - 70, 100, 1, canvas, "", 155, "", 0)

    def video_surface(self, frame):
        height, width, layers = frame.shape
        ratio = self.heights / height
        new_w = int(width * ratio)
        screen = pygame.Surface((new_w, self.heights))
        screen.fill([0, 0, 0])
        frame = cv2.resize(frame, (new_w, self.heights))
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = np.rot90(frame)
        frame = pygame.surfarray.make_surface(frame)
        screen.blit(frame, (0, 0))
        self.canvas.blit(screen, (self.x, (self.true_height - self.heights) // 2))
        self.camera.render()
        display_text_middle(None, 30, "Capture", (255, 255, 255), self.canvas, self.camera)


def file_read(file):
    pkl_file = open(file, "rb")
    json_data = pickle.load(pkl_file)
    pkl_file.close()
    return json_data


def file_write(datas, file):
    output = open(file, 'wb')
    pickle.dump(datas, output)
    output.close()


def food_natural_progress(plate, food):
    query_string = "1 {0} {1}".format(plate, food)
    data_require = nix_client.natural(q=query_string)['foods'][0]
    return data_require


def exercise_natural_progess(time, unit, exercise):
    query_string = "{0} {1} {2}".format(time, unit, exercise)
    data_require = nix_client.exercise(q=query_string)
    return data_require


def autocomplete_search_bar(query):
    data_require = nix_client.autocomplete(q=query)
    return data_require


def item_search_bar(query):
    data_require = nix_client.item(q=query)
    return data_require


def food_search_index(query):
    food_search = nix.search(q=query, results="0:1").json()
    return food_search
