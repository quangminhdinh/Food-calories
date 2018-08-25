import sys
from render_canvas import *
from pygame.locals import *


# from clarifai_api_request import *


class Scene7:

    def __init__(self, canvas, width, height):
        self.canvas = canvas
        self.image = pygame.image.load(os.path.join('data', 'background.png'))
        self.logo = pygame.image.load(os.path.join('data', 'white-logo.png')).convert_alpha()
        self.temp = pygame.image.load(os.path.join('temp.jpg'))

        data_json = [
            {"id": 309, "name": "Zinc, Zn", "value": 0, "unit": "mg"},
            {"id": 255, "name": "Water", "value": 0, "unit": "g"},
            {"id": 430, "name": "Vitamin K (phylloquinone)", "value": 0, "unit": "Âµg"},
            {"id": 573, "name": "Vitamin E added", "value": 0, "unit": "mg"},
            {"id": 323, "name": "Vitamin E (alpha-tocopherol)", "value": 0, "unit": "mg"},
            {"id": 326, "name": "Vitamin D3 (cholecalciferol)", "value": 0, "unit": "Âµg"},
            {"id": 325, "name": "Vitamin D2 (ergocalciferol)", "value": 0, "unit": "Âµg"},
            {"id": 328, "name": "Vitamin D (D2 + D3)", "value": 0, "unit": "Âµg"},
            {"id": 324, "name": "Vitamin D", "value": 0, "unit": "IU"},
            {"id": 401, "name": "Vitamin C, total ascorbic acid", "value": 0, "unit": "mg"},
            {"id": 415, "name": "Vitamin B-6", "value": 0, "unit": "mg"},
            {"id": 578, "name": "Vitamin B-12, added", "value": 0, "unit": "Âµg"},
            {"id": 418, "name": "Vitamin B-12", "value": 0, "unit": "Âµg"},
            {"id": 320, "name": "Vitamin A, RAE", "value": 0, "unit": "Âµg"},
            {"id": 318, "name": "Vitamin A, IU", "value": 0, "unit": "IU"},
            {"id": 510, "name": "Valine", "value": 0, "unit": "g"},
            {"id": 509, "name": "Tyrosine", "value": 0, "unit": "g"},
            {"id": 501, "name": "Tryptophan", "value": 0, "unit": "g"},
            {"id": 204, "name": "Total lipid (fat)", "value": 0, "unit": "g"},
            {"id": 342, "name": "Tocopherol, gamma", "value": 0, "unit": "mg"},
            {"id": 343, "name": "Tocopherol, delta", "value": 0, "unit": "mg"},
            {"id": 341, "name": "Tocopherol, beta", "value": 0, "unit": "mg"},
            {"id": 502, "name": "Threonine", "value": 0, "unit": "g"},
            {"id": 404, "name": "Thiamin", "value": 0, "unit": "mg"},
            {"id": 263, "name": "Theobromine", "value": 0, "unit": "mg"},
            {"id": 269, "name": "Sugars, total", "value": 0, "unit": "g"},
            {"id": 210, "name": "Sucrose", "value": 0, "unit": "g"},
            {"id": 638, "name": "Stigmasterol", "value": 0, "unit": "mg"},
            {"id": 209, "name": "Starch", "value": 0, "unit": "g"},
            {"id": 307, "name": "Sodium, Na", "value": 0, "unit": "mg"},
            {"id": 518, "name": "Serine", "value": 0, "unit": "g"},
            {"id": 317, "name": "Selenium, Se", "value": 0, "unit": "Âµg"},
            {"id": 405, "name": "Riboflavin", "value": 0, "unit": "mg"},
            {"id": 319, "name": "Retinol", "value": 0, "unit": "Âµg"},
            {"id": 203, "name": "Protein", "value": 0, "unit": "g"},
            {"id": 517, "name": "Proline", "value": 0, "unit": "g"},
            {"id": 306, "name": "Potassium, K", "value": 0, "unit": "mg"},
            {"id": 636, "name": "Phytosterols", "value": 0, "unit": "mg"},
            {"id": 305, "name": "Phosphorus, P", "value": 0, "unit": "mg"},
            {"id": 508, "name": "Phenylalanine", "value": 0, "unit": "g"},
            {"id": 410, "name": "Pantothenic acid", "value": 0, "unit": "mg"},
            {"id": 406, "name": "Niacin", "value": 0, "unit": "mg"},
            {"id": 506, "name": "Methionine", "value": 0, "unit": "g"},
            {"id": 428, "name": "Menaquinone-4", "value": 0, "unit": "Âµg"},
            {"id": 315, "name": "Manganese, Mn", "value": 0, "unit": "mg"},
            {"id": 214, "name": "Maltose", "value": 0, "unit": "g"},
            {"id": 304, "name": "Magnesium, Mg", "value": 0, "unit": "mg"},
            {"id": 505, "name": "Lysine", "value": 0, "unit": "g"},
            {"id": 337, "name": "Lycopene", "value": 0, "unit": "Âµg"},
            {"id": 338, "name": "Lutein + zeaxanthin", "value": 0, "unit": "Âµg"},
            {"id": 504, "name": "Leucine", "value": 0, "unit": "g"},
            {"id": 213, "name": "Lactose", "value": 0, "unit": "g"},
            {"id": 503, "name": "Isoleucine", "value": 0, "unit": "g"},
            {"id": 303, "name": "Iron, Fe", "value": 0, "unit": "mg"},
            {"id": 521, "name": "Hydroxyproline", "value": 0, "unit": "g"},
            {"id": 512, "name": "Histidine", "value": 0, "unit": "g"},
            {"id": 516, "name": "Glycine", "value": 0, "unit": "g"},
            {"id": 211, "name": "Glucose (dextrose)", "value": 0, "unit": "g"},
            {"id": 601, "name": "Cholesterol", "value": 0, "unit": "mg"},
            {"id": 301, "name": "Calcium, Ca", "value": 0, "unit": "mg"},
            {"id": 262, "name": "Caffeine", "value": 0, "unit": "mg"},
            {"id": 221, "name": "Alcohol, ethyl", "value": 0, "unit": "g"}
        ]
        # temp_data = file_read("nutrition_temp.pkl")
        # self.temp = get_image_from_food_database(temp_data[0])
        # self.data_nutrition = food_natural_progress(temp_data[1], temp_data[2])

        self.activate = True
        self.width = width
        self.heights = height

    def render(self):
        display_image(self.image, 0, 0, self.width, self.heights, self.canvas)
        # display_image(self.logo, (self.width - self.logo.get_width()) // 2,
        #               (self.height - self.logo.get_height()) // 2 - 50, self.logo.get_width(),
        #               self.logo.get_height(), self.canvas)
        display_image(self.temp, 150, 150, self.temp.get_width() // 2, self.temp.get_height() // 2, self.canvas)
        # self.submit.render()
        # display_text_middle(None, 30, "Get information", (255, 255, 255), self.canvas, self.submit)

    def active(self):
        if self.activate:
            fps_clock = pygame.time.Clock()
            mouse_pos = (0, 0)
            scene1_render = True
            while scene1_render:
                self.render()
                check = False
                if check:
                    pygame.mouse.set_cursor(*pygame.cursors.diamond)
                else:
                    pygame.mouse.set_cursor(*pygame.cursors.arrow)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                        pygame.quit()
                        sys.exit()
                    elif event.type == MOUSEMOTION:
                        mouse_pos = pygame.mouse.get_pos()
                pygame.display.update()
                fps_clock.tick(200)


width1 = 1327
height1 = 700
pygame.init()
display_surf = pygame.display.set_mode((width1, height1))
scene1 = Scene7(display_surf, width1, height1)
scene1.active()
