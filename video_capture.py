import cv2, os, time
from tqdm import tqdm

name = "DEAP_video1_2"
if not os.path.exists(name):
    os.mkdir(name)

# cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture('D:\\DEAP\\DEAP_dataset\\DEAP-video\\s01_trial01.avi')
timestamps = []
for idx in tqdm(range(3000)):
    ret, frame = cap.read()
    timestamps += [str(time.time())]

    cv2.imshow('Camera', frame)
    cv2.imwrite(f"{name}/{idx}.png", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

f = open(f"{name}/my-timestamps.txt", "w")
f.write(",".join(timestamps))
f.close()