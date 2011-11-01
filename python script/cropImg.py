#!/usr/bin/python
# -*- coding: UTF-8 -*-
from __future__ import division
import Image 
from math import ceil, floor
from Image import EXTENT  
 
import os  
import sys  
import string
from os import getcwd
		
		
def ProcessFile(aFile):  
	mTuple = os.path.split(aFile)  
	curdir = mTuple[0];  
	fileName = mTuple[1];  
	extendName = fileName.split('.').pop()
	print curdir  
	print fileName  
	print extendName  
	# if extendName =='h':  
	#     inp = open(aFile,'r')  
	#     for mLine in inp.readlines():  
	#         if(mLine.find(targetStr) != -1):  
	#             print aFile  
	#             print mLine  
	#             print "**************************"  
	#         else :  
	#             continue	
	if extendName == "gif" or extendName == "bmp" or extendName == "jpg" or extendName == "GIF" or extendName == "BMP" or extendName == "JPG":  
		im = Image.open(aFile)   #打开原始图片
		xsize, ysize = im.size 
		CropImg(im,fileName,'100')
		CropImg(im.resize((int(xsize/2.0),int(ysize/2.0)),Image.ANTIALIAS),fileName,'50')
		CropImg(im.resize((int(xsize/4.0),int(ysize/4.0)),Image.ANTIALIAS),fileName,'25')

def CropImg(im,fileName,resolutionPercentage):
	xsize, ysize = im.size          
	print xsize,ysize
	Fix_X = 256
	Fix_Y = 256
	V_SPLITE = int(ceil(xsize / Fix_X)) 
	H_SPLITE = int(ceil(ysize / Fix_Y))
	# V_SPLITE = 4
	# H_SPLITE = 4
	# print V_SPLITE,H_SPLITE
	
	for i in range (0, V_SPLITE ):
		for j in range ( 0 , H_SPLITE ):
			if Fix_X == 0:
				xtile = xsize/V_SPLITE
			else:
				xtile = Fix_X
			if Fix_Y == 0:
				ytile = ysize/H_SPLITE
			else:
				ytile = Fix_Y
			# print xtile,ytile
			# print i,j
			
			w = xtile
			h = ytile
			tx = (i+1)*xtile
			if tx > xsize:
				tx = xsize
				w = xsize % Fix_X
			ty = (j+1)*ytile
			if ty > ysize:
				ty = ysize
				h = ysize % Fix_Y
			box = (i*xtile, j*ytile, tx, ty)
			# print box
			
			im_temp = Image.new('RGB',(w,h))
			
			region = im.crop(box) 
			im_temp.paste(region,(0,0))
			# # im_temp.show()
			print "%s_"%fileName.split('.')[0]+"%s"%resolutionPercentage+"_%s"%i+"_%s"%j+".jpg" 
			im_temp.save("//Users//nasa127//cropout"+"//"+"%s_"%fileName.split('.')[0]+"%s"%resolutionPercentage+"_%s"%i+"_%s"%j+".jpg" , "JPEG")
			print "save OK" 
	print "picture file:" + fileName

def TraverseDir(aPath):  
    mList = os.listdir(aPath)  
    for mPath in mList:  
        tPath = os.path.join(aPath,mPath)  
        if os.path.isfile(tPath):  
            print tPath  
            ProcessFile(tPath)  
        else :  
            print tPath  
            TraverseDir(tPath)

TraverseDir('//Users//nasa127//Desktop//_out//mz')