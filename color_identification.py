import cv2
import numpy as np

def getcolor(img):
        
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # red color
    red_lower = np.array([136,87,111],np.uint8)
    red_upper = np.array([180,255,255],np.uint8)

    # blue color
    blue_lower = np.array([99,115,150],np.uint8)
    blue_upper = np.array([110,255,255],np.uint8)

    # yellow color
    yellow_lower = np.array([22,60,200],np.uint8)
    yellow_upper = np.array([60,255,255],np.uint8)

    # white color
    white_lower = np.array([0,0,200],np.uint8)
    white_upper = np.array([180,20,255],np.uint8)
    
    # black color
    black_lower = np.array([0,0,0],np.uint8)
    black_upper = np.array([180,255,30],np.uint8)
    
    # green color
    green_lower = np.array([36, 50, 70],np.uint8)
    green_upper = np.array([89, 255, 255],np.uint8)
    

    # all color together
    red = cv2.inRange(hsv, red_lower, red_upper)
    blue = cv2.inRange(hsv, blue_lower, blue_upper)
    yellow = cv2.inRange(hsv, yellow_lower, yellow_upper)
    white = cv2.inRange(hsv, white_lower, white_upper)
    black = cv2.inRange(hsv, black_lower, black_upper)
    green = cv2.inRange(hsv, green_lower, green_upper)


    # Morphological Transform, Dilation

    kernal = np.ones((11,11), "uint8")

    red = cv2.dilate(red, kernal)
    res_red = cv2.bitwise_and(img, img, mask = red)

    blue = cv2.dilate(blue, kernal)
    res_blue = cv2.bitwise_and(img, img, mask = blue)

    yellow = cv2.dilate(yellow, kernal)
    res_yellow = cv2.bitwise_and(img, img, mask = yellow)

    white = cv2.dilate(white, kernal)
    res_white = cv2.bitwise_and(img, img, mask = white)

    results = []

    black = cv2.dilate(black, kernal)
    res_black = cv2.bitwise_and(img, img, mask = black)

    green = cv2.dilate(green, kernal)
    res_green = cv2.bitwise_and(img, img, mask = green)
    
    AREA_Thr = 4000

    # Tracking red
    (contours, hierarchy)=cv2.findContours(red, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > AREA_Thr):
            x, y, w, h = cv2.boundingRect(contour)
            results.append(["Red",area,(x,y,w,h)]) 

    # Tracking blue
    (contours, hierarchy)=cv2.findContours(blue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > AREA_Thr):
            x, y, w, h = cv2.boundingRect(contour)
            results.append(["Blue",area,(x,y,w,h)]) 
            

    # Tracking yellow
    (contours, hierarchy)=cv2.findContours(yellow, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > AREA_Thr):
            x, y, w, h = cv2.boundingRect(contour)
            results.append(["Yellow",area,(x,y,w,h)]) 
            

    # Tracking white
    (contours, hierarchy)=cv2.findContours(white, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > AREA_Thr):
            x, y, w, h = cv2.boundingRect(contour)
            results.append(["White",area,(x,y,w,h)])

    # Tracking black
    (contours, hierarchy)=cv2.findContours(black, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > AREA_Thr):
            x, y, w, h = cv2.boundingRect(contour)
            results.append(["Black",area,(x,y,w,h)]) 

    # Tracking green

    (contours, hierarchy)=cv2.findContours(green, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > AREA_Thr):
            x, y, w, h = cv2.boundingRect(contour)
            results.append(["Green",area,(x,y,w,h)]) 

    if(len(results)):
        output= max(results,key= lambda x: x[1])
        return output[0]
    else:
        return "Not_Found"
