#!/usr/bin/env python3
#New file created
import os
import sys
from shutil import make_archive
from multiprocessing import Pool


current_dir= sys.argv[1]

#i need to accept a filepath like object as input. Look this up in os



def create_archive(current_dir):
    
    archive_name = os.path.join(str(current_dir), 'myarchive')
   
    root_dir = os.getcwd()
    return make_archive(archive_name, 'gztar', root_dir=root_dir)


if __name__ == '__main__':
    with Pool(5) as p:
        p.map(create_archive,[current_dir])

        





