#!/usr/bin/env python3
#New file created
#this will create a new bash script. Takes filename as a system args, don't forger .sh file extension
# when naming the file.
import os
import sys
filename=sys.argv[1]
bash_shebang = "#!/bin/bash"
if not os.path.exists(filename):
    with open(filename, "w")as f:
        f.write(bash_shebang)
        f.write("\n#New file created\n") 
else:
    print("Error, the file {} already exists!".format(filename))
    sys.exit(1)