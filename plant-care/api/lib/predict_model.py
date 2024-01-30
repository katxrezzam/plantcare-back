import tensorflow as tf
from tensorflow.keras.models import load_model
from pathlib import Path

import numpy as np

class_names = ["Potato Early Blight", "Potato Late Blight", "Potato Healthy"]
target_size = (224, 224)


def get_route():
    current_path = Path(__file__).resolve().parent
    images_path = current_path.parent.parent.joinpath("images")
    return images_path


def predict(image_name):
    model = load_model("crop_classification.keras")

    image_path = f"{get_route()}\\{image_name}"
    img = tf.keras.utils.load_img(image_path, target_size=target_size)
    img_array = tf.keras.utils.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)

    prediction = model.predict(img_array)

    score = tf.nn.softmax(prediction[0])

    return class_names[np.argmax(score)], 100 * np.max(score)
