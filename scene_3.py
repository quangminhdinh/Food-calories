import sys
from render_canvas import *
from pygame.locals import *


class Scene3:

    def __init__(self, canvas, width, height):
        self.canvas = canvas
        self.image = pygame.image.load(os.path.join('data', 'background.png'))
        self.logo = pygame.image.load(os.path.join('data', 'white-logo.png')).convert_alpha()

        self.name = Button(600, 50, 460, 100, (155, 255, 155, 155), 2, canvas, "Name", 255,
                           "Please fill in this field!", (255, 155, 155, 155))
        self.age = Button(600, 50, 460, 180, (155, 255, 155, 155), 2, canvas, "Age", 255,
                          "Please fill in this field!", (255, 155, 155, 155))
        self.gender = DropDown(["Male", "Female"], 600, 50, 460, 260, canvas, (55, 155, 55, 155), (255, 255, 255),
                               (50, 155, 50, 255))
        self.weight = Button(600, 50, 460, 420, (155, 255, 155, 155), 2, canvas, "Weight (kg)", 255,
                             "Please fill in this field!", (255, 155, 155, 155))
        self.height = Button(600, 50, 460, 500, (155, 255, 155, 155), 2, canvas, "Height (cm)", 255,
                             "Please fill in this field!", (255, 155, 155, 155))
        self.lifestyle = DropDown(["Sedentary lifestyle", "Slightly active lifestyle", "Moderately active lifestyle",
                                   "Active lifestyle", "Very active lifestyle"], 600, 50, 460, 340, canvas,
                                  (55, 155, 55, 155), (255, 255, 255), (50, 155, 50, 255))
        self.submit = Button(200, 50, 860, 580, 0, 1, canvas, "", 205, "", 0)

        self.blur = Button(width - 40, height - 40, 20, 20, (255, 255, 255, 58), 2, canvas, "", 255, "", (0, 0, 0, 0))
        self.activate = True
        self.width = width
        self.heights = height

    def render(self):
        display_image(self.image, 0, 0, self.width, self.heights, self.canvas)
        # display_image(self.logo, (self.width - self.logo.get_width()) // 2,
        #               (self.height - self.logo.get_height()) // 2 - 50, self.logo.get_width(),
        #               self.logo.get_height(), self.canvas)
        # self.blur.render()

        self.name.render()
        display_text(self.name.x + 20, (self.name.h - 20) // 2 + self.name.y, None, 25, self.name.value,
                     (255, 255, 255), self.canvas)
        display_text(180, 115, None, 30, "Username", (255, 255, 255), self.canvas)

        self.age.render()
        display_text(self.age.x + 20, (self.age.h - 20) // 2 + self.age.y, None, 25, self.age.value,
                     (255, 255, 255), self.canvas)
        display_text(180, 195, None, 30, "Age", (255, 255, 255), self.canvas)

        self.weight.render()
        display_text(self.weight.x + 20, (self.weight.h - 20) // 2 + self.weight.y, None, 25, self.weight.value,
                     (255, 255, 255), self.canvas)
        display_text(180, 435, None, 30, "Weight", (255, 255, 255), self.canvas)

        self.height.render()
        display_text(self.height.x + 20, (self.height.h - 20) // 2 + self.height.y, None, 25, self.height.value,
                     (255, 255, 255), self.canvas)
        display_text(180, 515, None, 30, "Height", (255, 255, 255), self.canvas)

        self.submit.render()
        display_text_middle(None, 25, "Submit", (255, 255, 255), self.canvas, self.submit)

        self.lifestyle.render()
        display_text(180, 355, None, 30, "Lifestyle", (255, 255, 255), self.canvas)

        self.gender.render()
        display_text(180, 275, None, 30, "Gender", (255, 255, 255), self.canvas)

    def active(self):
        if self.activate:
            num_component_list = [self.weight, self.height, self.age]
            dropdown_component_list = [self.gender, self.lifestyle]
            fps_clock = pygame.time.Clock()
            mouse_pos = (0, 0)
            scene1_render = True
            active_component = None
            counter = 0
            while scene1_render:
                self.render()
                now = pygame.time.get_ticks()
                if now - counter >= 400 and active_component is not None:
                    counter = now
                    if active_component.value.endswith("|"):
                        active_component.value = active_component.value[:-1]
                    else:
                        active_component.value += "|"
                if active_component is not None:
                    active_component.alpha = (155, 255, 155, 155)
                check = False
                allow_input = True
                if self.name.activate(mouse_pos):
                    check = True
                else:
                    for nlc in num_component_list:
                        if nlc.activate(mouse_pos):
                            check = True
                            break
                    if not check:
                        if self.submit.activate(mouse_pos):
                            check = True
                        else:
                            for rd in dropdown_component_list:
                                if rd.main_box.activate(mouse_pos):
                                    check = True
                                    break
                                else:
                                    for tbn in rd.buttons:
                                        if tbn.activate(mouse_pos) and rd.activate:
                                            check = True
                                            break
                if check:
                    pygame.mouse.set_cursor(*pygame.cursors.diamond)
                else:
                    pygame.mouse.set_cursor(*pygame.cursors.arrow)
                for drp in dropdown_component_list:
                    for nbt in drp.buttons:
                        if nbt.activate(mouse_pos) and drp.activate:
                            nbt.alpha = (0, 155, 0, 255)
                        else:
                            nbt.alpha = (50, 155, 50, 255)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                        pygame.quit()
                        sys.exit()
                    elif event.type == MOUSEBUTTONUP:
                        allow_input = False
                        if self.name.activate(mouse_pos):
                            if active_component is not None and active_component.value.endswith("|"):
                                active_component.value = active_component.value[:-1]
                            active_component = self.name
                            allow_input = True
                        elif self.submit.activate(mouse_pos):
                            if active_component is not None and active_component.value.endswith("|"):
                                active_component.value = active_component.value[:-1]
                            allow = True
                            for ncl in num_component_list:
                                if ncl.value == "":
                                    ncl.error = "Please fill in this field!"
                                else:
                                    try:
                                        float(ncl.value)
                                    except ValueError:
                                        ncl.value = ""
                                        ncl.error = "Please enter a number!"
                                if ncl.value == "":
                                    allow = False
                                    ncl.alpha = (255, 155, 155, 155)
                            if self.name.value == "":
                                allow = False
                                self.name.alpha = (255, 155, 155, 155)
                                self.name.error = "Please fill in this field!"
                            if allow:
                                profile_data = {
                                    "name": self.name.value,
                                    "age": self.age.value,
                                    "height": self.height.value,
                                    "weight": self.weight.value,
                                    "gender": self.gender.value,
                                    "lifestyle": self.lifestyle.value
                                }
                                file_write(profile_data, "profile.pkl")
                                scene1_render = False
                        else:
                            for com in num_component_list:
                                if com.activate(mouse_pos):
                                    if active_component is not None and active_component.value.endswith("|"):
                                        active_component.value = active_component.value[:-1]
                                    active_component = com
                                    allow_input = True
                                    break
                            lk = True
                            deactivate_other = None
                            for dr in dropdown_component_list:
                                if dr.main_box.activate(mouse_pos):
                                    lk = False
                                    dr.activate = (dr.activate is False)
                                    deactivate_other = dr
                                    break
                                for index, btn in enumerate(dr.buttons):
                                    if btn.activate(mouse_pos) and dr.activate:
                                        dr.value = dr.text[index]
                                        dr.activate = False
                                        break
                            if lk:
                                for cr in dropdown_component_list:
                                    if cr.activate:
                                        cr.activate = False
                            else:
                                if deactivate_other is not None:
                                    for cc in dropdown_component_list:
                                        if cc != deactivate_other:
                                            cc.activate = False
                    elif event.type == KEYDOWN and active_component is not None:
                        if active_component.value.endswith("|"):
                            active_component.value = active_component.value[:-1]
                        if event.key == K_RETURN:
                            pass
                        elif event.key == K_BACKSPACE:
                            active_component.value = active_component.value[:-1]
                        else:
                            if get_text_parameter(None, 30, active_component.value, (0, 0, 0)).get_width() < 650:
                                active_component.value += event.unicode
                    elif event.type == MOUSEMOTION:
                        mouse_pos = pygame.mouse.get_pos()
                if not allow_input:
                    if active_component is not None and active_component.value.endswith("|"):
                        active_component.value = active_component.value[:-1]
                    active_component = None
                if active_component is not None:
                    active_component.alpha = (155, 200, 155, 155)
                    pygame.draw.rect(self.canvas, (155, 255, 155), (active_component.x, active_component.y,
                                                                    active_component.w, active_component.h), 1)
                pygame.display.update()
                fps_clock.tick(200)


width1 = 1327
height1 = 700
pygame.init()
display_surf = pygame.display.set_mode((width1, height1))
scene1 = Scene3(display_surf, width1, height1)
scene1.active()
