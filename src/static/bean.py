from cv2 import VideoCapture, CAP_DSHOW, FONT_HERSHEY_SIMPLEX, CAP_PROP_FRAME_HEIGHT, CAP_PROP_FRAME_WIDTH, imshow, waitKey, destroyAllWindows, putText, LINE_AA, line, rectangle, SimpleBlobDetector_create, cvtColor, drawKeypoints, DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS, SimpleBlobDetector_Params, COLOR_BGR2GRAY
import numpy as np

print("LAUNCHING. . .")
print("PRODUCED BY BOTCH CO, A SUBSIDIARY OF BRADLEY JAKE NIELSON INDUSTRIES")

# configure settings
camWidth = 1280
camHeight = 720
font = FONT_HERSHEY_SIMPLEX
lineColor = (51,204,51)
textColor = (51,204,51)
xMargin = 250
yMargin = 250

# initialize video capture
camNumber = int(input("camera index: "))
cap = VideoCapture(camNumber, CAP_DSHOW)

# wait for capture to start
while not cap.isOpened():
    pass

# set video capture resolution
cap.set(CAP_PROP_FRAME_WIDTH, camWidth)
cap.set(CAP_PROP_FRAME_HEIGHT, camHeight)

# initialize default crop settings
targetX = int(camWidth / 2)
targetY = int(camHeight / 2)



'''blob stuf'''
# Setup SimpleBlobDetector parameters.
params = SimpleBlobDetector_Params()
 
# Change thresholds
params.minThreshold = 10
params.maxThreshold = 200
 
# Filter by Area.
params.filterByArea = True
params.minArea = 1500
 
# Filter by Circularity
params.filterByCircularity = True
params.minCircularity = 0.05
 
# Filter by Convexity
params.filterByConvexity = True
params.minConvexity = 0.6
 
# Filter by Inertia
params.filterByInertia = True
params.minInertiaRatio = 0.005

detector = SimpleBlobDetector_create(params)

# run continously
while True:
    # get an image from webcam
    status, newImage = cap.read()
    proccessImage = cvtColor(newImage.copy(), COLOR_BGR2GRAY)

    # do bean counting
    blobs = detector.detect(proccessImage)
    beans = len(blobs)
    newImage = drawKeypoints(newImage, blobs, np.array([]), lineColor, DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    # display stats
    putText(newImage, "Camera " + str(camNumber) + ":", (20, 50), font, 2, textColor, 4, LINE_AA)
    putText(newImage, f"BRADLEY JAKE NEILSON INDUSTRIES", (20, 90), font, 0.75, textColor, 2, LINE_AA)
    putText(newImage, f"BEAN COUNT: {beans} beans", (20, 120), font, 0.75, textColor, 2, LINE_AA)
    putText(newImage, f"CEN: {targetX}, {targetY}", (20, 150), font, 0.75, textColor, 2, LINE_AA)
    putText(newImage, f"WID: {xMargin * 2}", (20, 180), font, 0.75, textColor, 2, LINE_AA)
    putText(newImage, f"HEI: {yMargin * 2}", (20, 210), font, 0.75, textColor, 2, LINE_AA)
    putText(newImage, f"RES: {camWidth}, {camHeight}", (20, 240), font, 0.75, textColor, 2, LINE_AA)

    # draw crosshairs and box
    line(newImage, (targetX - 20, targetY), (targetX + 20, targetY), lineColor, 2)
    line(newImage, (targetX, targetY - 20), (targetX, targetY + 20), lineColor, 2) 
    rectangle(newImage, (targetX - xMargin, targetY - yMargin), (targetX + xMargin, targetY + yMargin), lineColor, 2)
    
    # display image
    imshow("B.E.A.N", newImage)

    key = waitKey(1)
    #if a key was pressed
    if key != -1:
        # press x to exit
        if key == ord('x'):
            destroyAllWindows()
            break