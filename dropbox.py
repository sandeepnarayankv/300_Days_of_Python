import os

import dropbox
from dotenv import load_dotenv


load_dotenv()
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
dbx = dropbox.Dropbox('ACCESS_TOKEN')

files = [f for f in os.listdir('./') if os.path.isfile(os.path.join('./', f))]
print(files)

# with open("justimage.webp", 'rb') as f:
#     content = f.read()
#     d.files_upload(content, file_name)