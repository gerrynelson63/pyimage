from exif import Image

from datetime import datetime

file="2022-05-07-16-29-0023.jpg"
dir="/home/sasgnn/images/ConthroughHighSchool"

with open(dir+'/'+file, 'rb') as image_file:
    my_image = Image(image_file)
    hasexif=my_image.has_exif
    print(hasexif)
    exif_list=my_image.list_all()
    print(exif_list)
    now = datetime.now()
    my_image.datetime=now