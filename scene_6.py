import sys
from render_canvas import *
from pygame.locals import *


from clarifai_api_request import *


class Scene6:

    def __init__(self, canvas, width, height):
        self.canvas = canvas
        self.image = pygame.image.load(os.path.join('data', 'background.png'))
        self.logo = pygame.image.load(os.path.join('data', 'white-logo.png')).convert_alpha()
        self.temp = pygame.image.load(os.path.join('temp.jpg'))

        self.predictions = DropDown(clarifai_workflow_detect(), 300, 50, 950, 150, canvas,
                                    (55, 155, 55, 155), (255, 255, 255), (50, 155, 50, 255))
        self.plate = DropDown(["Bowl", "Plate", "Cup", "Oz", "Tbsp", "Slice"], 300, 50, 950, 250, canvas,
                              (55, 155, 55, 155), (255, 255, 255), (50, 155, 50, 255))
        self.again = Button(400, 70, 850, 400, (50, 155, 50, 85), 2, canvas, "", 255, "", (0, 0, 0, 0))
        self.submit = Button(400, 70, 850, 550, (50, 155, 50, 85), 2, canvas, "", 255, "", (0, 0, 0, 0))

        self.activate = True
        self.width = width
        self.heights = height

    def render(self):
        display_image(self.image, 0, 0, self.width, self.heights, self.canvas)
        # display_image(self.logo, (self.width - self.logo.get_width()) // 2,
        #               (self.height - self.logo.get_height()) // 2 - 50, self.logo.get_width(),
        #               self.logo.get_height(), self.canvas)
        display_image(self.temp, 150, 150, self.temp.get_width(), self.temp.get_height(), self.canvas)
        self.submit.render()
        display_text_middle(None, 30, "Get information", (255, 255, 255), self.canvas, self.submit)
        self.again.render()
        display_text_middle(None, 30, "Capture again", (255, 255, 255), self.canvas, self.again)
        display_text(850, 240, None, 30, "Unit", (255, 255, 255), self.canvas)
        self.plate.render()
        display_text(850, 160, None, 30, "Predict", (255, 255, 255), self.canvas)
        self.predictions.render()

    def active(self):
        if self.activate:
            fps_clock = pygame.time.Clock()
            mouse_pos = (0, 0)
            scene1_render = True
            while scene1_render:
                self.render()
                check = False
                if self.again.activate(mouse_pos) or self.submit.activate(mouse_pos) or \
                        self.plate.main_box.activate(mouse_pos) or self.predictions.main_box.activate(mouse_pos):
                    check = True
                elif self.plate.activate:
                    for i in self.plate.buttons:
                        if i.activate(mouse_pos):
                            check = True
                            break
                elif self.predictions.activate:
                    for i in self.predictions.buttons:
                        if i.activate(mouse_pos):
                            check = True
                            break
                if check:
                    pygame.mouse.set_cursor(*pygame.cursors.diamond)
                else:
                    pygame.mouse.set_cursor(*pygame.cursors.arrow)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                        pygame.quit()
                        sys.exit()
                    elif event.type == MOUSEBUTTONUP:
                        plate_off = True
                        predict_off = True
                        if self.again.activate(mouse_pos) and not self.predictions.activate and not self.plate.activate:
                            return 5
                        elif self.submit.activate(mouse_pos) and not self.predictions.activate and not \
                                self.plate.activate:
                            fid = post_image_to_food_database()
                            food_model_train(self.predictions.value)
                            file_write([fid, self.plate.value, self.predictions.value], "nutrition_temp.pkl")
                            return 7
                        elif self.plate.main_box.activate(mouse_pos):
                            self.plate.activate = (self.plate.activate is False)
                            plate_off = False
                        elif self.predictions.main_box.activate(mouse_pos):
                            self.predictions.activate = (self.predictions.activate is False)
                            predict_off = False
                        elif self.plate.activate:
                            for index, pre in enumerate(self.plate.buttons):
                                if pre.activate(mouse_pos):
                                    self.plate.value = self.plate.text[index]
                                    break
                        elif self.predictions.activate:
                            for index, pre in enumerate(self.predictions.buttons):
                                if pre.activate(mouse_pos):
                                    self.predictions.value = self.predictions.text[index]
                                    break
                        if plate_off:
                            self.plate.activate = False
                        if predict_off:
                            self.predictions.activate = False
                    elif event.type == MOUSEMOTION:
                        mouse_pos = pygame.mouse.get_pos()
                pygame.display.update()
                fps_clock.tick(200)


width1 = 1327
height1 = 700
pygame.init()
display_surf = pygame.display.set_mode((width1, height1))
scene1 = Scene6(display_surf, width1, height1)
scene1.active()
