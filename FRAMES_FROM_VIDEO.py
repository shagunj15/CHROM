import os
import cv2


def extractFrames(pathIn, dirName):
    # Create target Directory if don't exist
    if not os.path.exists(dirName):
        os.mkdir(dirName)
    else:
        print("Directory ", dirName, " already exists")
    try:
        # Change the current working Directory
        os.chdir(dirName)
    except OSError:
        print("Can't change the Current Working Directory")

    cap = cv2.VideoCapture(pathIn)
    counter = 0
    while (True):
        # reading from frame
        ret, frame = cap.read()
        if ret:
            # if video is still left continue creating images
            name = dirName + '//' + 'frame' + str(counter) + '.jpg'
            print('Creating...' + name)

            # writing the extracted images
            cv2.imwrite(name, frame)

            counter += 1
        else:
            break
    # Release all space and windows once done
    cap.release()
    cv2.destroyAllWindows()

rootdir = r'C:\Users\ppjoh\Desktop\DEAP\DEAP_dataset'
folders = os.listdir(rootdir)
for f in folders:
    for vid in os.listdir(os.path.join(rootdir,f)):
        pathin = os.path.join(rootdir,f,vid)
        dirname = pathin[:-4]
        extractFrames(pathin,dirname)
