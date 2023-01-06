# import dependencies

from google.cloud import vision
import io
from glob import glob
from os.path import splitext, basename
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="CREDENTIAL/FILEPATH/HERE.json"
# https://stackoverflow.com/questions/45501082/set-google-application-credentials-in-python-project-to-use-google-api

# Detecting the text of one image
def detect_text(path):
    """Detects text in the file."""
    client = vision.ImageAnnotatorClient()

    # [START vision_python_migration_text_detection]
    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations

    caption = ""
    
    for text in texts:
        caption+= text.description

    return caption
  
# Adding captions to dataframe
filenames = []
ImgText = []

for filepath in glob('FOLDER/WHERE/IMAGES/ARE/STORED/*'):
    filenames.append(splitext(basename(filepath))[0])
    ImgText.append(detect_text(filepath))
    
    
ImageURLS = Mdf["image_file"].tolist() # Mdf as defined https://github.com/acidicgaseouscloud/BlockChainMemes/blob/main/PushShift24CAT.py

captionsForDF = []

counter = -1 # count starts from 0
    
for url in ImageURLS:
    counter+=1
    for filename in filenames:
        if filename in url:  
          captionsForDF.append(ImgText[counter])
        else:
          captionsForDF.append("No Text Detected")
          
Mdf["Captions"] = captionsForDF
