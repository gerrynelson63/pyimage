from exif import Image as ExifImage

from datetime import datetime

import argparse, sys, subprocess, os, json

parser = argparse.ArgumentParser(description="Update exif image metadata.")
parser.add_argument("-d","--directory", help="Directory that contains JSON files to import",default="/home/sasgnn/images/ConthroughHighSchool")
parser.add_argument("-q","--quiet", help="Suppress the are you sure prompt.", action='store_true')
args= parser.parse_args()

basedir=args.directory

if os.path.isdir(basedir):

    # loop files in the directory
    for filename in os.listdir( basedir ):
        img_file=os.path.join(basedir,filename)
        with open(img_file, 'rb') as image_file:
           my_image = ExifImage(image_file)

           hasexif=my_image.has_exif
           print(hasexif)
           exif_list=my_image.list_all()
           print(exif_list)

        print ("Processing File: "+img_file) 
        for tag in exif_list:
            # Get the Value of the Tag in the Image
            value = my_image.get(tag)

            # Print the Tag/Value Pair to the Terminal Window
            print("{}: {}".format(tag, value))
        
        now = datetime.now()
        my_image.datetime="1999:05:06 22:00:07"

        output_filepath=os.path.join("/tmp/test",filename)

        with open(output_filepath,'wb') as ofile:
            ofile.write(my_image.get_file())
""" 
for root, dirs, file_names in os.walk(dir):
        for file_name in file_names:
            if file_name.lower().endswith(('jpg', 'png')):
                img_path = os.path.join(root, file_name)
                fix_image_dates(img_path) """