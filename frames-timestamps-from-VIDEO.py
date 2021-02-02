# D:\\DEAP\\DEAP_dataset\\DEAP-video\\s01_trial01.avi

import cv2
MS = []
cameraCapture = cv2.VideoCapture('D:\\DEAP\\DEAP_dataset\\DEAP-video\\s01_trial01.avi')
file = open("sample-text.txt", "w")
success, frame = cameraCapture.read()
while success:
    #if cv2.waitKey(1) == 27:
        #break
    cv2.imshow('Test camera', frame)
    success, frame = cameraCapture.read()
    milliseconds = cameraCapture.get(cv2.CAP_PROP_POS_MSEC)
    microseconds = milliseconds * 1000

    '''
    seconds = milliseconds//1000
    milliseconds = milliseconds%1000
    minutes = 0
    hours = 0
    if seconds >= 60:
        minutes = seconds//60
        seconds = seconds % 60

    if minutes >= 60:
        hours = minutes//60
        minutes = minutes % 60
    '''
    MS.append(microseconds)
    print('milliseconds:', microseconds)
    ms = str(microseconds)
    file.write(ms + ",")

cv2.destroyAllWindows()
cameraCapture.release()

print(len(MS))

