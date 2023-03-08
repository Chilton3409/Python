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
        shutil.copy(src=input('Enter a file to copy'), dst=input('enter file destination'))
        print("your file {} has been moved to {}".format(str(src), str(dst)))

        return 
    def copyall(self, src):
        shutil.copytree(src=input('Enter directory to copy\n'), dst=input('direcory\n'), dirs_exist_ok=True)

    def makezip(self):
        shutil.make_archive(base_name=input("enter name for new zip file\n"), root_dir=input('Enter root or starting point\n'), format='zip')


    def arg(self):
        self.arguments.add_argument('-z', '--zip', action='store_true', help='helper text') 

        args = self.arguments.parse_args()

        if args.zip:
            self.makezip()
        
def main():
    x = Moving()
    x.arg()



if __name__=='__main__':
    with Pool(5) as p:
        p.map(main(), [])

        