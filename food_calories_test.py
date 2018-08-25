from render_canvas import *

# data_require = food_natural_progress("", "ch")
# data_require = food_search_index("pizza")
data_require = item_search_bar("'f762ef22-e660-434f-9")
# data_require = exercise_natural_progess("10", "kilometers", "jumping")
# data_require = autocomplete_search_bar("cho")

print(data_require)
# print()
# from clarifai.rest import ClarifaiApp
# from clarifai.rest import Workflow
# from clarifai.rest import Image as ClImage
#
# app = ClarifaiApp(api_key='970e14f749704c77886abf5932001150')
# model = app.models.get('General')
# image = ClImage(url='https://samples.clarifai.com/metro-north.jpg')
# model.predict([image])

# img2 = ClImage(url='http://www.savourydays.com/wp-content/uploads/2013/01/PhoBoHN.jpg', concepts=['pho'], not_concepts=['metro', 'station'])
# model = app.models.create('pho', concepts=['pho'])
# new_model = app.models.get('pho')
# new_model.train()


# app = ClarifaiApp(api_key='970e14f749704c77886abf5932001150')
#
# img1 = ClImage(url="https://samples.clarifai.com/metro-north.jpg")
# img2 = ClImage(url="https://samples.clarifai.com/puppy.jpeg")
# img3 = ClImage(url="http://www.savourydays.com/wp-content/uploads/2013/01/PhoBoHN.jpg")
#
# app.inputs.bulk_create_images([img1, img2, img3])
# # print(A)
# B = app.inputs.search_by_predicted_concepts(concept_id='9277838c3e75400f8952045ce339837e')
# print(B)

# from clarifai_api_request import *
# from render_canvas import *
# print(food_natural_progress("bowl", "soup"))

