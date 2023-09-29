import cv2
import numpy as np

#function for drawing line
def drawLine(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    #thresholds of the color
    lower_red1 = np.array([0, 175, 175])
    upper_red1 = np.array([5, 255, 255])

    lower_red2 = np.array([175, 175, 175])
    upper_red2 = np.array([180, 255, 255])
    
    #need 2 masks since red wraps around 180 mark
    mask = cv2.inRange(hsv, lower_red1, upper_red1)
    mask = mask + cv2.inRange(hsv, lower_red2, upper_red2)

    #find contours of red regions
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    centers = []
    for i in contours:
        M = cv2.moments(i)
        if M["m00"] != 0:
            cX = M["m10"]/M["m00"]
            cY = M["m01"]/M["m00"]
            centers.append((cX, cY))

    #linear regression on all the points to find line
    mean_x = sum(x for x, y in centers)/len(centers)
    mean_y = sum(y for x, y in centers)/len(centers)

    numerator = sum((x-mean_x)*(y-mean_y) for x, y in centers)
    denominator = sum((x-mean_x)**2 for x, y in centers)

    slope = numerator/denominator
    intercept = mean_y-(slope*mean_x)

    #plot line and return the image
    cv2.line(image, (0, int(intercept)), (int(image.shape[1]), int(slope*image.shape[1]+intercept)), (0, 0, 255), 2)
    return image

img = cv2.imread("/Users/patrickli/Documents/Code/CodingChallenges/perceptionChallenge/red.png")
#print(img.shape)

#split image in half
width = img.shape[1]
width = width//2

s1 = img[:, :width]
s2 = img[:, width:]

#call function on both sides, then merege two images
s1 = drawLine(s1)
s2 = drawLine(s2)
img = np.concatenate((s1, s2), axis=1)

cv2.imwrite("answer.png", img)
'''
cv2.imshow("result", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''