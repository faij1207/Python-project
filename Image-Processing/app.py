import base64
import requests
from urllib.request import urlretrieve
from PIL import Image
api_url="https://python-api.techsimplus.com/api/amazon-service/"
service=int(input("enter your service 1.for feace detection 2. for celebrity detection 3.object detection"))
#rb=read in byte
if service==1: 
    with open('download.jpg','rb')as imagr_file:
        base64_bytes=base64.b64encode(imagr_file.read())
        base64_string=base64_bytes.decode()
        response=requests.post(api_url, json ={"image":base64_string,"service_type":"CelebrityDetection"})
        response=response.json()

elif service==2:
    with open('download.jpg','rb')as imagr_file:
        base64_bytes=base64.b64encode(imagr_file.read())
        base64_string=base64_bytes.decode()
        response=requests.post(api_url, json ={"image":base64_string,"service_type":"FaceDetection"})
        response=response.json()
elif service==3:
    with open('download.jpg','rb')as imagr_file:
        base64_bytes=base64.b64encode(imagr_file.read())
        base64_string=base64_bytes.decode()
        response=requests.post(api_url, json ={"image":base64_string,"service_type":"ObjectDetection"})
        response=response.json()
else:
    print("wrong service")
image_url=response['data']['image']
urlretrieve(image_url,'processed_img.png')
image=Image.open('processed_img.png')
image.show()