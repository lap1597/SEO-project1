import requests
import pprint
from IPython.display import Image, display
import json
from PIL import Image
from io import BytesIO

import os

def get_geolocation(api_key, ip_address):
    url = f"https://ipgeolocation.abstractapi.com/v1/?api_key={api_key}&ip_address={ip_address}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def create_ascii(img_path):
  pic = Image.open(img_path)
  width, height = pic.size
  aspect_ratio = height / width
  new_width = 110
  new_height = int(aspect_ratio * new_width)
  img = pic.resize((new_width, new_height))
  img = img.convert('L')
  pixels = img.getdata()
  chars = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.', ' ']
  count = len(chars)
  new_pixels = [chars[int(((count-1)*pixel)/256)] for pixel in pixels] 
  new_pixels = ''.join(new_pixels)
  new_pixels_count = len(new_pixels)
  ascii_image = [new_pixels[index:index + new_width] for index in range(0, new_pixels_count, new_width)]
  ascii_image = '\n'.join(ascii_image)
  return ascii_image + '\n'

def download_image(url,save_path):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img.save(save_path)
    return save_path

#"870a3e4f506c4354ac76f4bf6c2051b3" 

def main():
    api_key ="870a3e4f506c4354ac76f4bf6c2051b3" 

    while True:
        ip_address = input("Enter a random IP address - example: xxx.xxx.xxx.xxx (or 'exit' to quit): ")
        if ip_address.lower() == 'exit':
            break
        geolocation_data = get_geolocation(api_key, ip_address)
        if geolocation_data:
            pprint.pprint(geolocation_data)
            # img_url = geolocation_data['flag']['png'] 
            # if img_url.startswith('https'):
            #     save_directory ='/SEO-project1/pic/'
            #     os.makedirs(save_directory, exist_ok=True)  # Ensure the directory exists
            #     img_path = os.path.join(save_directory, 'flag.png')
            #     download_image(img_url, img_path)
            #     print(create_ascii(img_path))
        else:
            print("Failed to retrieve data. Please check the IP address and try again.")


if __name__ == "__main__":
    main()

