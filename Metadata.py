#!/usr/bin/env python
#-*- coding: UTF-8 -*-
import sys
from PIL.ExifTags import TAGS
from PIL import Image

def testForExif(imgFile):
	exifData = {}
	info = imgFile._getexif()
	if info:
		for (tag,value) in info.items():
			decoded = TAGS.get(tag, tag)
			exifData[decoded] = value
		for campo,valor in exifData.items():
			print '[+] ' + str(campo) + ' : ' + str(valor)
	else:
		print "No se han encontrado metadatos."

photo = Image.open(sys.argv[1])
if (photo.format == 'JPEG'):
	testForExif(photo)
else:
	print "Introduce una imagen con extensión JPEG"
