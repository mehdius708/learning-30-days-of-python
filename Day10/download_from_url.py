import requests
import os
import shutil
from download_util import download_file

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DOWNLOADS_DIR = os.path.join(BASE_DIR, "downloads")
downloaded_img_path = os.path.join(DOWNLOADS_DIR, '1.jpg')

os.makedirs(DOWNLOADS_DIR, exist_ok=True)

url = "https://i.hurimg.com/i/hdn/75/0x0/5dcd630a0f25441794d60a1c.jpg"

# Small item we used requests lib
#r = requests.get(url, stream = True)
#r.raise_for_status()

#with open(downloaded_img_path, 'wb') as f:
    #f.write(r.content)

# bigger item we used shutil lib

#dl_filename=os.path.basename(url)
#new_dl_path = os.path.join(DOWNLOADS_DIR, dl_filename)

#with requests.get(url, stream = True) as r:
#    with open(new_dl_path, 'wb') as file_obj:
#        shutil.copyfileobj(r.raw, file_obj)

download_file(url, DOWNLOADS_DIR, 'test.jpg')
