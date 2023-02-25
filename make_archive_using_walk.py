#!/usr/bin/env python3
#New file created
import os
import sys
from shutil import make_archive
from multiprocessing import Pool


current_dir= sys.argv[1]

#i need to accept a filepath like object as input. Look this up in os



def create_archive(current_dir):
    for root, dirs, files in os.walk(".", topdown = True):
        for name in files:
            print(os.path.join(root,name))
            for name in dirs:
                print(os.path.join(root,name))
                
    


if __name__ == '__main__':
    with Pool(5) as p:
        p.map(create_archive,[current_dir])