#!/usr/bin/env python3
#New file created
import sys
import shutil
from multiprocessing import Pool
import argparse


class Moving():
    def __init__(self):
        self.arguments = argparse.ArgumentParser(description="requests package",formatter_class=argparse.ArgumentDefaultsHelpFormatter)
        self.files = []
        

    def move_file(self, src, dst):
        shutil.copy(src=input('Enter a file to copy\n'), dst=input('enter file destination\n'))
        print("your file {} has been moved to {}".format(str(src), str(dst)))

        return 
    def copyall(self, src):
        shutil.copytree(src=input('Enter directory to copy\n'), dst=input('direcory\n'), dirs_exist_ok=True)

    def removedir(self):
        shutil.rmtree(path=input('enter path to file to delete'))

    def makezip(self):
        shutil.make_archive(base_name=input("enter name for new zip file\n"), root_dir=input('Enter root or starting point\n'), format='zip')


    def arg(self):
        self.arguments.add_argument('-z', '--zip', action='store_true', help='Enter new filename, then enter root dir to start.') 
        self.arguments.add_argument('-c', '--copy', action='store_true', help='enter src, then enter destination')
        self.arguments.add_argument('-d', '--delete', action='store_true', help="Enter filepath for deletion")

        args = self.arguments.parse_args()

        if args.zip:
            self.makezip()

        if args.copy:
            self.move_file()
        
        if args.delete:
            self.removedir()

def main():
    x = Moving()
    x.arg()



if __name__=='__main__':
    with Pool(5) as p:
        p.map(main(), [])

        