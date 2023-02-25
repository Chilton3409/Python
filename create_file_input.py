#!/usr/bin/env python3
#New file created
#!/usr/bin/env python3
#New file created
from multiprocessing import Pool
import os
import sys

#filename=sys.argv[1]

shebang = "#!/usr/bin/env python3"
def create_file(file):

    if not os.path.exists(file):
        with open(file, "w")as f:
            f.write(shebang)
            f.write("\n#New file created\n") 
            print("the file {} has been created.".format(file))
    else:
        print("Error, the file {} already exists!".format(file))
        sys.exit(1)



create_file(file=input("enter the name of your file: \n"))