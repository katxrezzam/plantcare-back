from rest_framework.decorators import api_view
from rest_framework.response import Response
from .lib.predict_model import predict
from .lib.handle_image import save_image, remove_image
from .lib.handle_gpt import handle_responses


@api_view(["POST"])
def upload_image(request):
    try:
        image_file = request.data["image"]
        file_name = image_file.name

        if not image_file:
            return Response({"Error": "Image not found"}, status=400)

        if not save_image(image_file):
            return Response({"Error": "Error saving file"}, status=500)

        disease, score = predict(file_name)

        remove_image(image_file)

        return Response({"disease": disease, "score": score})
    except Exception as e:
        print(f"An error ocurred during prediction {e}")
        return Response({"Error": "An error ocurred during prediction"}, status=500)


@api_view(["POST"])
def chat(request):
    try:
        message = request.data["message"]

        if not message:
            return Response({"Error": "Empty message"}, status=400)
        reply = handle_responses(message)
        return Response({"response": reply})
    except Exception as e:
        print(f"An error ocurred loading your message {e}")
        return Response({"Error": "An error ocurred loading your message"}, status=500)
