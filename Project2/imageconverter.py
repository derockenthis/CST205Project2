import requests
import urllib.request

r = requests.post(
    "https://api.deepai.org/api/colorizer",
    files={
        'image': open('jetImage3.jpg', 'rb'),
    },
    headers={'api-key': 'b8c5d118-0549-4884-b765-79798f16fa00'}
)
print(r.json())
print(r.json()['output_url'])

urllib.request.urlretrieve(r.json()['output_url'], "local-filename.jpg")
