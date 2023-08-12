import cv2

img = cv2.imread("solar-system.jpg")
cv2.putText(img,"Sun",(2,250),cv2.FONT_HERSHEY_COMPLEX,1.5,(255,255,255),2)
cv2.putText(img,"Mercury",(100,180),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
cv2.putText(img,"Venus",(170,250),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
cv2.putText(img,"Earth",(270,180),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
cv2.putText(img,"Mars",(370,250),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
cv2.putText(img,"Jupiter",(550,180),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
cv2.putText(img,"Saturn",(730,300),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
cv2.putText(img,"Uranus",(950,300),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
cv2.putText(img,"Neptune",(1100,300),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2) 
cv2.imshow("output",img) 

cv2.waitKey(10000)
