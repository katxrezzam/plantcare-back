from PIL import Image
import os


def save_image(image_file):
    try:
        image = Image.open(image_file)
        image_path = f"images/{image_file.name}"
        image.save(image_path)
        return True
    except Exception as e:
        print(f"Error saving image: {str(e)}")
        return False


def remove_image(image_file):
    try:
        image_path = f"images/{image_file.name}"
        os.remove(image_path)
        return True
    except Exception as e:
        print(print(f"Error deleting image: {str(e)}"))
        return False
