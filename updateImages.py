from exif import Image as ExifImage

from datetime import datetime

import argparse, sys, filedate, os, time

parser = argparse.ArgumentParser(description="Update exif image metadata.")
parser.add_argument("-id","--directory", help="Directory that contains Image files to update",default="/home/sasgnn/images/ConthroughHighSchool")
parser.add_argument("-od","--output", help="Directory to output new files.",default="/home/sasgnn/test")
parser.add_argument("-dt","--datetime", help="Datetime to set on Image",default="1999:05:06 12:00:00")

parser.add_argument("-q","--quiet", help="Suppress the are you sure prompt.", action='store_true')
args= parser.parse_args()

basedir=args.directory
outputdir=args.output
newdatetime=args.datetime

# get date parts for setting  file creation and modify time
dateparts=newdatetime.split(":")

year=int(dateparts[0])
month=int(dateparts[1])
day=int(dateparts[2].split(" ")[0])

hour=12
minute=30
second=30

date = datetime(year=year, month=month, day=day, hour=hour, minute=minute, second=second)
modTime = time.mktime(date.timetuple())

# directory ?
if os.path.isdir(basedir):

    # loop files in the directory
    for filename in os.listdir( basedir ):
        img_file=os.path.join(basedir,filename)
        with open(img_file, 'rb') as image_file:
           my_image = ExifImage(image_file)

        hasexif=my_image.has_exif
        #print(hasexif)
        exif_list=my_image.list_all()
        print(exif_list)

        print ("Processing File: "+img_file) 
        # for tag in exif_list:
        #     # Get the Value of the Tag in the Image
        #     value = my_image.get(tag)

        #     # Print the Tag/Value Pair to the Terminal Window
        #     print("{}: {}".format(tag, value))
        
        # set exif dat time attributes
        my_image.datetime_original=newdatetime
        my_image.datetime=newdatetime
        my_image.usercomment="Scanned by Connie"

        output_filepath=os.path.join(outputdir,filename)
        
        # write the image to the target directory
        with open(output_filepath,'wb') as ofile:
            ofile.write(my_image.get_file())

        # get new exif data    
        with open(output_filepath, 'rb') as new_image_file: 
            new_image = ExifImage(new_image_file)
        
        exif_list2=new_image.list_all()
        
        # print new exif data
        for tag in exif_list2:
            # Get the Value of the Tag in the Image
            value = new_image.get(tag)

            # Print the Tag/Value Pair to the Terminal Window
            print("{}: {}".format(tag, value))
        
        # update create and modify date of new file

        os.utime(output_filepath, (modTime, modTime))    
        


""" 
for root, dirs, file_names in os.walk(dir):
        for file_name in file_names:
            if file_name.lower().endswith(('jpg', 'png')):
                img_path = os.path.join(root, file_name)
                fix_image_dates(img_path) """