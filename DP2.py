import sys

sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')


import numpy as np
import cv2


point1 = []
point2 = []

def get_mouse_clicks(event, x, y, flags, params):
    global point1
    global point2
    if event == cv2.EVENT_LBUTTONDOWN:
        print ('Point clicked: {}, {}'.format(x, y))
        if not point1:
            point1 = [x, y]
        else:
            point2 = [x, y]
            dx = point1[0] - point2[0]
            dy = point1[1] - point2[1]
            dist = np.sqrt(dx**2 + dy**2)
            print ('Distance = {0:2.2f}'.format(dist))
            point1 = []
            point2 = []
        
        


if __name__ == '__main__':

    cap = cv2.VideoCapture(0)

    cv2.namedWindow("frame")
    cv2.setMouseCallback("frame", get_mouse_clicks)

    while(cap.isOpened()):
        ret, img = cap.read()
        cv2.imshow('frame', img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()    