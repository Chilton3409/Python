#!/usr/bin/env python3
# New file created
import os
from statistics import quantiles
import sys
import glob

from PIL import Image
import enhancements 
import move_file_input
import file_task
import archive_with_input
import archive_fresh
from multiprocessing import Pool
from PIL import ImageFilter
from PIL import ImageOps
#move these enhancements into its own module and call it from there later nater.
#todo's optional small preview and maybe asking what to name it,lol nah....
#to tun place all files in the pwd, and then call ../ like so ../basic_imageapp ../
#and then ../ for archive and source,
#as of now I need to loojk for the archive it is making.

#todo's also just creating thumbails at the same time?
class ImageApp():
    def __init__(self):
        self.files = []
        self.old_files = []
        self.thumbnails = []

    def unpack(self):
        dst=input("Where would you like to store these files: \n")
        for file in self.files:
            file_task.move_file(src=str(file), dst=dst)
            print("The file {} has been moved to {}.".format(file, dst))
            
    def sources(self,):
             dst=input("Where would you like to store the originals: \n")
             for file in self.old_files:
                file_task.move_file(src=str(file), dst=dst)
                print("The file {} has been moved to {}.".format(file, dst))


  

    def delete_originals(self):
        pass
    #I want to pass in self.old_files and delete each on in the list


    
 






    def create_images(self, infile=str()):
        os.listdir(infile)
        for infile in glob.glob("*.JPG"):
            outfile = os.path.splitext(infile)[0] + "_edited.jpg"
          
            if infile != outfile:
                try:
                    with Image.open(infile) as im:
                    #im1 = im.filter(ImageFilter.DETAIL)
                    #could optionally call more than one image filter function
                    #functions above are only expecting an image object and return one also.
                    
                        im = enhancements.enhance_detail(im)
                        


                        #enhancements.create_thumbnail(im)
                        #todo, move old_files to or do something to solve 
                        #duplicates problem
                        
                        im.save(outfile, "JPEG", quality='maximum', subsampling=0,)
                        #thumb = enhancements.create_thumbnail(im)
                        
                        self.files.append(outfile)
                        
                        self.old_files.append(infile)
                        #self.thumbnails.append(thumb)
                     
                        #file_task.move_file(str(outfile), 'black_white')

            #print(infile)
                except OSError:
                    print("cannot create thumbnail for", infile)

                
                print(self.files)
        

if __name__=='__main__':
   x = ImageApp()
   x.create_images(infile=input("Enter source directory of photos you want edited. \n"))
   x.unpack()
   x.sources()

 




