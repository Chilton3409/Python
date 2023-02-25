#!/usr/bin/env python3
#New file created
import sys
import shutil


def move_file(src, dst):
    shutil.copy(src, dst)
    print("your file {} has been moved to {}".format(src, dst))
    return 
move_file(src=input("enter source: \n"), dst=input("enter destination"))