#!/usr/bin/env python3
#New file created
# in this example will create a gziped tat file containing all the files found within 
#my current documentation directory
import os
from shutil import make_archive

#thinking about turning the archive name into a system argument
#then you could create a backup of any folder and its children real quick like
#I think this could be kool for a variety of different reasons
#and then add multiprocessing to increase the overall speed
#turn this into a function


archive_name = os.path.join(os.getcwd(), 'myarchive')
current_dir = os.chdir("../")
root_dir = os.chdir("../")

make_archive(archive_name, 'gztar', root_dir=root_dir)

