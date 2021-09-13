import requests
import json

url = "https://www.flickr.com/services/rest/?method\
=flickr.photos.getPopular&api_key=8ecccdaeb5e81de8c102ec2\
85bf1f938&user_id=193935247@N06&format=json"


response = requests.request("GET", url)

print(response.text)
if response.status_code == 200:
    print("\nRequest Successful")
else:
    print("Bad Request")
