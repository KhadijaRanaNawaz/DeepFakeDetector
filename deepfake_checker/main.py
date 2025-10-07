# main.py

from deepfake_model import CheckDeepFake

image_path = "static/real/source/Child.jpg"
# image_path = "static/fakes/deepfakeChild.png"
is_fake = CheckDeepFake(image_path)

print(f"Is the image a deepfake? {'Yes' if is_fake else 'No'}")