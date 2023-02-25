#!/usr/bin/env python3
#New file created
from multiprocessing import Pool
import os
import sys

filename=sys.argv[1]
shebang = "#!/usr/bin/env python3"
def create_file(filename):

    if not os.path.exists(filename):
        with open(filename, "w")as f:
            f.write(shebang)
            f.write("\n#New file created\n") 
    else:
        print("Error, the file {} already exists!".format(filename))
        sys.exit(1)


if __name__ == '__main__':
    with Pool(5) as p:
        p.map(create_file,[filename])

