import cv2
import numpy as np
import time

 
c = cv2.VideoCapture("sample2.mp4")
_,f = c.read()
timeot = time.time()+ 23 ;


avg1 = np.float32(f)
avg2 = np.float32(f)
background = np.float32(avg2)
# img = np.load('temp.npy');
# img=img.reshape(240,426,3)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
f_array = []
i=0;
while(1):
	_,f = c.read()
	# cv2.accumulateWeighted(f,avg1,0.05)
	# res1 = cv2.convertScaleAbs(avg1)
	cv2.accumulateWeighted(f,avg2,0.01)
	res2 = cv2.convertScaleAbs(avg2)
	#res2 = cv2.cvtColor(f,cv2.COLOR_BGR2GRAY)
	print (f.shape)
	f = cv2.cvtColor(f,cv2.COLOR_BGR2GRAY)

	#cv2.accumulateWeighted(res2,background,0.01)
	#res3 = cv2.convertScaleAbs(background)
	#img = img.reshape(240,426,3)
	cv2.imshow('img',f)

	# temp = cv2.subtract(f,img)
	

	# blur = cv2.GaussianBlur(temp,(5,5),0)
	# ret,th=cv2.threshold(blur, 0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
	cv2.imshow('avg2',res2)

	if time.time()>timeot:

	  	f_array+=[res2]
	  	print ("success")
	  	break;

	k = cv2.waitKey(20)

	if k == 27:
	    break

#print(arrayofavg.shape)
np.save('temp.npy',np.array(f_array))
cv2.destroyAllWindows()
c.release()


