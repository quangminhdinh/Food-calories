from clarifai.rest import ClarifaiApp
from clarifai.rest import Workflow

CLARIFAI_DETECT_API_KEY = "f3f988543ee84fd4b9403f028859c9f0"
CLARIFAI_DATABASE_API_KEY = "e0e75fcd842a469abe0a7dadc3180d49"
CLARIFAI_WORKFLOW_ID = "main-workflow"
CLARIFAI_MODEL_ID = "train_model"
app = ClarifaiApp(api_key=CLARIFAI_DETECT_API_KEY)
cl_database = ClarifaiApp(api_key=CLARIFAI_DATABASE_API_KEY)
workflow = Workflow(app.api, workflow_id=CLARIFAI_WORKFLOW_ID)
model = app.models.get(model_id=CLARIFAI_MODEL_ID)

TEMP_IMG = "temp.jpg"


def clarifai_workflow_detect():
    data_get = workflow.predict_by_filename(TEMP_IMG)['results'][0]['outputs'][0]['data']['concepts']
    data_value = []
    if len(data_get) <= 8:
        for data_dict in data_get:
            data_value.append(data_dict['name'])
    else:
        for index in range(8):
            data_value.append(data_get[index]['name'])
    return data_value


def food_model_train(food_concept):
    app.inputs.create_image_from_filename(TEMP_IMG, concepts=[food_concept])
    model.add_concepts([food_concept])
    model.train()


def post_image_to_food_database():
    dtb_id = cl_database.inputs.create_image_from_filename(TEMP_IMG).input_id
    return dtb_id


def get_image_from_food_database(dtb_id):
    img = cl_database.inputs.get(dtb_id)
    return img.url


food_model_train("minhdz")
