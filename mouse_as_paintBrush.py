import cv2
import numpy as np
def measure(event,x,y,glags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),100,(0,255,255),5)
        for i in range(3):
            cv2.rectangle(img,(x,y),(x+150,y+150),(255,255,0),3)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, 'Mouse-as-a-PushButtton', (x-5, y-5), font, 1, (255, 0, 255), 1, cv2.LINE_AA)

cv2.namedWindow('image')
img=np.zeros((1024,1024,3),dtype='float32')
cv2.setMouseCallback('image',measure)
while True:
    cv2.imshow('image',img)
    if cv2.waitKey(5)==55:
        break
cv2.destroyAllWindows()



















# OR you can rubn this to saw the Different results

#
# import cv2
# import numpy as np
#
# def draw(event,x,y,flags,param):
#
#     if event==cv2.EVENT_LBUTTONDOWN:
#         cv2.circle(img,(x,y),5,(0,255,0),2)
#         # cv2.rectangle(img,(x,y),(x+30,y+30),(255,255,0),5)
# cv2.namedWindow('window')
# img=np.zeros((512,512,3),dtype='float32')
# cv2.setMouseCallback('window',draw)
# while True:
#     cv2.imshow("window",img)
#     if cv2.waitKey(9)==29:
#         break
# cv2.destroyAllWindows()
#

