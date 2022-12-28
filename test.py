from exif import Image

dir="/home/sasgnn/images/ConthroughHighSchool"

with open('grand_canyon.jpg', 'rb') as image_file:
    my_image = Image(image_file)
    my_image.has_exif
