#This uses an api from DeepApi to convert the image from color to black and white, it also retrieves the link from the json and downloads the image.
import requests
import urllib.request

r = requests.post("https://api.deepai.org/api/colorizer",files={'image': open('girlnoise.png', 'rb'),},headers={'api-key': 'b8c5d118-0549-4884-b765-79798f16fa00'})
print(r.json())
print(r.json()['output_url'])

print(urllib.request.urlretrieve(r.json()['output_url'])[0])
