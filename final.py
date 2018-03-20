import cv2
import numpy as np
import predict_density as pd
import time

templ = np.load('temp.npy');
templ_new=templ.reshape(templ.shape[1],templ.shape[2],3)
templ_new= cv2.cvtColor(templ_new, cv2.COLOR_BGR2GRAY)
print (templ_new.shape)
video = cv2.VideoWriter('video11.avi',cv2.VideoWriter_fourcc(*'PIM1'),25,(720,1280) , 1)

timeout = time.time()+50
vid = cv2.VideoCapture("sample2.mp4")
while True:

	_,f = vid.read()


	f_new = pd.image_preprocess(f)
	img_sub = cv2.subtract(f_new,templ_new)
	
	cv2.imshow('Original', f)
	density,image = pd.pre_den(img_sub)
	cv2.imshow('Video',image)
	print (density),


	video.write(image)

	if time.time()>timeout:
		break
	k = cv2.waitKey(20)

	if k == 27:
	    break


cv2.destroyAllWindows()
vid.release()







