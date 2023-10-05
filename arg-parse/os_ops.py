#!/usr/bin/env python3
#New file created
import os 
import glob
import sys

class Operations():
    
    def __init__(self):
        self.files=[]
        
        
    def create_directory(dir_name):
        dir_name=os.makedirs(name=input("create new directory\n "))
        return 

    def delete_directory(delete_name):
        delete_name=os.removedirs(name=input("enter directory you want deleted \n"))
        return
    def list_files(self):
        #this will affect the destination of where files are written

        
        for infile in glob.glob("*.*"):
           return self.files.append(infile)


      
       

    #use this in combination with list_files to write files where you
    def create_file(*filename):
        filename=input("Enter the name of your new file \n")
        shebang = "#!/usr/bin/env python3"

        if not os.path.exists(filename):
            with open(filename, "w")as f:
                f.write(shebang)
                f.write("\n#New file {} created\n".format(filename)) 
        else:
            print("Error, the file {} already exists!".format(filename))
            sys.exit(1)

    def check_permissions():
        pass


    
    def unpack(self):
        for file in self.files:
            fi = os.path.splitext(file)
            
            print(fi[0], fi[1])
        return
                
def main():
    x = Operations()
    x.create_file()
    


   

if __name__=="__main__":
    main()



    
