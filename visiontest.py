import io
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/agabdelb/vision bot/secret-brushlands-95547/google_vidion.json'
# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

# Instantiates a client
client = vision.ImageAnnotatorClient()

# The name of the image file to annotate
file_name = os.path.join(
    os.path.dirname(__file__),
    'IMG_3723.JPG')

# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)

# Performs label detection on the image file
#response = client.label_detection(image=image)
#labels = response.label_annotations

response_faces = client.face_detection(image=image)
face_labels = response_faces.face_annotations

print face_labels

for face in face_labels:
	print face.joy_likelihood

"""
print('Labels:')
for label in labels:
    print(label.description)"""