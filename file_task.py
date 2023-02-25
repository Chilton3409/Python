#!/usr/bin/env python3
#New file created
import sys
import shutil
#shutil.copy('create_file_multicore.py', './practice_moving_files/')

def move_file(src, dst):
    shutil.copy(src, dst)
    print("your file {} has been moved to {}".format(str(src), str(dst)))
    return 


if __name__ == "__main__":
    move_file(str(sys.argv[1]), str(sys.argv[2]))



