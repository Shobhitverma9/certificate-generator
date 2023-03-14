from flask import Flask, jsonify, request
from flask_restful import Api
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import cloudinary
import cloudinary.uploader
import cloudinary.api
import json
from flask_cors import CORS
#Config
cloudinary.config(
  cloud_name = "dy1hexft1",
  api_key = "311744991862889",
  api_secret = "2uq-b8O_1WMASu06UY5Kj5WsLmg",
  secure = True
)


myFont = ImageFont.truetype('calibri.ttf', size=40)

def makeCertificate(data):
    W, H = (1920,1080)
    msg = data['name']
    im = Image.open('cert.png')
    draw = ImageDraw.Draw(im)
    _, _, w, h = draw.textbbox((1100, 500),msg, font=myFont)
    draw.text(((W-w)/2, (H-h)/2), msg,font=myFont,fill='orange')

    im.save("hello5.png", "PNG")

def uploadImage(p_id):

  # Upload the image and get its URL
  # ==============================

  # Upload the image.
  # Set the asset's public ID and allow overwriting the asset with new versions
  cloudinary.uploader.upload("hello5.png", public_id=p_id, unique_filename = False, overwrite=True)

  # Build the URL for the image and save it in the variable 'srcURL'
  srcURL = cloudinary.CloudinaryImage(p_id).build_url()

  # Log the image URL to the console. 
  # Copy this URL in a browser tab to generate the image on the fly.
  print("****2. Upload an image****\nDelivery URL: ", srcURL, "\n")
  return srcURL

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST'])
def hello_world():
    data = request.json
    #print(data['name'])
    p_id = data['id']
    makeCertificate(data)
    url = uploadImage(p_id)
    return url
