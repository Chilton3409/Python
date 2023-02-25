#!/usr/bin/env python3
#New file created
from PIL import Image


from PIL import ImageFilter
from PIL import ImageOps
def enhance_detail(im):
    im = im.filter(ImageFilter.DETAIL)
    return im

def enhance_contour(im):
    im = im.filter(ImageFilter.CONTOUR)
    return im 

def enhance_3dColorLut(im):
    #need to look up size and table parameters that go with this function 
    im = im.filter(ImageFilter.Color3DLUT)
    return im 

def enhance_edges(im):
    im = im.filter(ImageFilter.EDGE_ENHANCE)
    return im 

def enhance_edges_more(im):
    im = im.filter(ImageFilter.EDGE_ENHANCE_MORE)
    return im

def create_thumbnail(im):
    size = (600, 400)
    im = im.thumbnail(size)
    return im
