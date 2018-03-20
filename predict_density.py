import cv2
import numpy as np
import matplotlib.pyplot as plt
import time


def pre_den(image):
	blur = cv2.GaussianBlur(image,(5,5),0)
	ret,th=cv2.threshold(blur, 0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
	#cv2.imshow('avg2',th)
	hist,bins = np.histogram(th.ravel(),256,[0,256])

	density = hist[255] / (hist[0] + hist[255])


	return (density,th)


def image_preprocess(image):
	image = np.array(cv2.cvtColor(image,cv2.COLOR_BGR2GRAY))
	print (image.shape[0])
	image = image.reshape(image.shape[0],image.shape[1])
	return image








	


