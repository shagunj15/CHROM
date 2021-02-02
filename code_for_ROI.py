import imutils
import numpy as np
import cv2
import dlib

image = cv2.imread(r'D:\DEAP\DEAP_dataset\s01_trial01\frame0.jpg')
print('image shape:',image.shape)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
detector = dlib.get_frontal_face_detector() # face detector
predictor = dlib.shape_predictor('D:\DEAP\DEAP_dataset\shape_predictor_68_face_landmarks.dat') #face detector
faces = detector(gray,1)
h = 100
for face in faces:
    landmarks = predictor(gray, face)
    x1 = landmarks.part(20).x
    y1 = landmarks.part(20).y
    x2 = landmarks.part(25).x
    y2 = landmarks.part(25).y

    cv2.rectangle(image, (x1, y1-h), (x2, y2), (0, 255, 0), 2)

print(x1, y1-h, x2, y2)
cv2.imshow("rectangle", image)

slicedImage = image[y1-h:y2, x1:x2]
#print(slicedImage)
#cv2.waitKey(0)

cv2.imshow("sliced image", slicedImage)


##### SKIN SELECTION PROCESS -> SKIN MASK INSIDE THE ROI #####
lower = np.array([0, 48, 80], dtype = "uint8") #upper and lower boundaries of skin
upper = np.array([20, 255, 255], dtype = "uint8") #of the HSV pixel intensities to be condidered skin
slicedImage = imutils.resize(slicedImage, width = 400)
converted = cv2.cvtColor(slicedImage, cv2.COLOR_BGR2HSV) #converting RGB to HSV
skinMask = cv2.inRange(converted, lower, upper) #upper and lower boundaries fo the HSV pixel intensities

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
skinMask = cv2.erode(skinMask, kernel, iterations = 2)
skinMask = cv2.dilate(skinMask, kernel, iterations = 2)
# blur the mask to help remove noise, then apply the mask to the frame
skinMask = cv2.GaussianBlur(skinMask, (3, 3), 0)
skin = cv2.bitwise_and(slicedImage, slicedImage, mask = skinMask)
# show the skin in the image along with the mask
# cv2.imshow("images", np.hstack([slicedImage, skin]))
cv2.imshow("final sliced image", skin)

# print('sliced image:',slicedImage)
# print('\nskin selected pixels:',skin)
# print('\nAverage of the skin pixels:',np.mean(skin))

### converting to BGR as openCV will read it as RGB
skin_BGR = cv2.cvtColor(skin, cv2.COLOR_HSV2BGR)
print('skin_BGR:',np.mean(skin_BGR[:,:,0]))
# Rn = skin_BGR[:,:,0]/np.mean(skin_BGR[:,:,0])
# Gn = skin_BGR[:,:,1]/np.mean(skin_BGR[:,:,1])
# Bn = skin_BGR[:,:,2]/np.mean(skin_BGR[:,:,2])
# print('Rn:',Rn)
# print('Gn:',Gn)
# print('Bn:',Bn)
# Xs = (3*Rn) - (2*Gn)
# Ys = (1.5*Rn) + Gn - (1.5*Bn)


cv2.waitKey(0)


