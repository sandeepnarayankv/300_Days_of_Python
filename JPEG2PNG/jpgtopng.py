from msilib.schema import Directory
from PIL import Image as img
import os, sys
strip_chr = "\\"
s_dir = sys.argv[1].strip(strip_chr)
t_dir = sys.argv[2].strip(strip_chr)
target = '.png'
source_dir = os.path.join(os.getcwd(), s_dir)
target_directory = os.path.join(source_dir, t_dir)
try:
    os.mkdir(target_directory)
except:
    print('Dir Exists')
for root, dirs, files in os.walk(source_dir):
    for filename in files:
        file, ext = os.path.splitext(filename)
        try:
            with img.open(os.path.join(root, filename)) as im:
                outfile = os.path.join(target_directory, file+target)
                im.save(outfile, "PNG")
        except OSError:
            print("cannot create png for", filename)