import cv2
import numpy as np
import statistics
import time
import sys
# camera = cv2.VideoCapture(0)  # init the camera
camera = cv2.VideoCapture("./external_programs/100_fast_1.mp4")
resolution = (480, 848)

flag = sys.argv[3]
size = int(sys.argv[2])
mw = size
mh = size + 1
marea = mw * mh
rate = 1

# print("max_area:::", marea)

def img_preprocessing1(img):
    # gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # img = gray
    # ret, thresh = cv2.threshold(gray,180,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    ret, thresh = cv2.threshold(img,130,255,cv2.THRESH_BINARY_INV)

    thresh = 255 - thresh
    # noise removal
    kernel = np.ones((1,1),np.uint8)
    opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 2)
    # sure background area
    sure_bg = cv2.dilate(opening,kernel,iterations=4)
    # Finding sure foreground area
    dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
    ret, sure_fg = cv2.threshold(dist_transform,0.3*dist_transform.max(),255,0)
    # Finding unknown region
    sure_fg = np.uint8(sure_fg)
    # cv2.imwrite("frames/" + str(i) + "__.jpg", fg)
    return thresh, sure_fg, sure_bg

def img_preprocessing(img):
    # gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # img = gray
    # ret, thresh = cv2.threshold(gray,180,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    ret, thresh = cv2.threshold(img,160,255,cv2.THRESH_BINARY_INV)

    thresh = 255 - thresh
    # noise removal
    kernel = np.ones((3,3),np.uint8)
    opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 2)
    # sure background area
    sure_bg = cv2.dilate(opening,kernel,iterations=1)
    # Finding sure foreground area
    dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
    ret, sure_fg = cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0)
    # Finding unknown region
    sure_fg = np.uint8(sure_fg)
    # cv2.imwrite("frames/" + str(i) + "__.jpg", fg)
    return thresh, sure_fg, sure_bg


def my_print(str):
    print('python-output(' + str + ')')


def main():
    ret, frame = camera.read()
    i = 0
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    count5 = 0
    count6 = 0
    count7 = 0
    count8 = 0
    count9 = 0
    count10 = 0
    count11 = 0
    count12 = 0
    areas = []

    while ret:
        # line = sys.stdin.readline()
        # if line == "terminate":
        #     my_print('I got a terminate request from electron (js)...terminating')
        #     exit(0)
        # else:
        ret, frame = camera.read()
        if i % 9 == 0:    
            offset = 53
            y1 = [0, 0 + offset]
            y2 = [200, 200 + 24 + offset]
            y3 = [400, 400 + 40 + offset]
            y4 = [600, 600 + 40 + offset]
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            # resize = cv2.resize(frame, (int(frame.shape[1]/rate), int(frame.shape[0]/rate)))  # resize the frame
            resize = cv2.resize(frame, resolution)
            gray = cv2.cvtColor(resize, cv2.COLOR_BGR2GRAY)
            # cv2.imshow('frame',gray)
            (thresh, sure_fg, sure_bg) = img_preprocessing(gray)
            sure_bg = 255 - sure_bg
            contours, hierarchy = cv2.findContours(
                    sure_bg, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            for c in contours:
                x, y, w, h = cv2.boundingRect(c)
                # if w < int(frame.shape[1]/rate) and h < int(frame.shape[0]/rate):
                if w < 50 and h < 50:
                    if y > y1[0] and y < y1[1]:
                        if w > mw and h <= mh:
                            count_in_area = int(w / mw) + 1
                            count1 += count_in_area
                        elif h > mh and w <= mw:
                            count_in_area = int(h / mh) + 1
                            count1 += count_in_area
                        elif h > mh and w > mw:
                            count_in_area1 = int(h / mh) + 1
                            count_in_area2 = int(w / mw) + 1
                            count_in_area = count_in_area1 * count_in_area2
                            count1 += count_in_area
                        else:
                            count1 += 1
                    elif y > y2[0] and y < y2[1]:
                        if w > mw and h <= mh:
                            count_in_area = int(w / mw) + 1
                            count2 += count_in_area
                        elif h > mh and w <= mw:
                            count_in_area = int(h / mh) + 1
                            count2 += count_in_area
                        elif h > mh and w > mw:
                            count_in_area1 = int(h / mh) + 1
                            count_in_area2 = int(w / mw) + 1
                            count_in_area = count_in_area1 * count_in_area2
                            count2 += count_in_area
                        else:
                            count2 += 1
                    elif y > y3[0] and y < y3[1]:
                        if w > mw and h <= mh:
                            count_in_area = int(w / mw) + 1
                            count3 += count_in_area
                        elif h > mh and w <= mw:
                            count_in_area = int(h / mh) + 1
                            count3 += count_in_area
                        elif h > mh and w > mw:
                            count_in_area1 = int(h / mh) + 1
                            count_in_area2 = int(w / mw) + 1
                            count_in_area = count_in_area1 * count_in_area2
                            count3 += count_in_area
                        else:
                            count3 += 1
                    elif y > y4[0] and y < y4[1]:
                        if w > mw and h <= mh:
                            count_in_area = int(w / mw) + 1
                            count4 += count_in_area
                        elif h > mh and w <= mw:
                            count_in_area = int(h / mh) + 1
                            count4 += count_in_area
                        elif h > mh and w > mw:
                            count_in_area1 = int(h / mh) + 1
                            count_in_area2 = int(w / mw) + 1
                            count_in_area = count_in_area1 * count_in_area2
                            count4 += count_in_area
                        else:
                            count4 += 1
        if i % 10 == 0: 
            offset = 77
            y1 = [0, 0 + offset]
            y2 = [200, 200 + 19 + offset]
            y3 = [400, 400 + 30 + offset]
            y4 = [600, 600 + 40 + offset]
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
            # print(i)   
            # resize = cv2.resize(frame, (int(frame.shape[1]/rate), int(frame.shape[0]/rate)))  # resize the frame
            resize = cv2.resize(frame, resolution)
            gray = cv2.cvtColor(resize, cv2.COLOR_BGR2GRAY)
            # cv2.imshow('frame',gray)
            (thresh, sure_fg, sure_bg) = img_preprocessing(gray)
            # sure_bg = 255 - sure_bg
            contours, hierarchy = cv2.findContours(
                    sure_bg, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            # print("=======", i, len(contours))
            # if i == 80:
            ccs = []
            for c in contours:
                x, y, w, h = cv2.boundingRect(c)
                # if w < int(frame.shape[1]/rate) and h < int(frame.shape[0]/rate):
                if w < 50 and h < 50:
                    ccs.append(c)
                    # print(w, h)
                    # img = cv2.rectangle(sure_bg, (x, y), (x+w, y+h),(0, 255, 0), 5)
                    # # cv2.imshow("rect", img)
                    # cv2.imshow("rect1", sure_bg)
                    # cv2.waitKey(0)
                    if y > y1[0] and y < y1[1]:
                        if w > mw and h <= mh:
                            count_in_area = int(w / mw) + 1
                            count5 += count_in_area
                        elif h > mh and w <= mw:
                            count_in_area = int(h / mh) + 1
                            count5 += count_in_area
                        elif h > mh and w > mw:
                            count_in_area1 = int(h / mh) + 1
                            count_in_area2 = int(w / mw) + 1
                            count_in_area = count_in_area1 * count_in_area2
                            count5 += count_in_area
                        else:
                            count5 += 1
                    elif y > y2[0] and y < y2[1]:
                        if w > mw and h <= mh:
                            count_in_area = int(w / mw) + 1
                            count6 += count_in_area
                        elif h > mh and w <= mw:
                            count_in_area = int(h / mh) + 1
                            count6 += count_in_area
                        elif h > mh and w > mw:
                            count_in_area1 = int(h / mh) + 1
                            count_in_area2 = int(w / mw) + 1
                            count_in_area = count_in_area1 * count_in_area2
                            count6 += count_in_area
                        else:
                            count6 += 1
                    elif y > y3[0] and y < y3[1]:
                        if w > mw and h <= mh:
                            count_in_area = int(w / mw) + 1
                            count7 += count_in_area
                        elif h > mh and w <= mw:
                            count_in_area = int(h / mh) + 1
                            count7 += count_in_area
                        elif h > mh and w > mw:
                            count_in_area1 = int(h / mh) + 1
                            count_in_area2 = int(w / mw) + 1
                            count_in_area = count_in_area1 * count_in_area2
                            count7 += count_in_area
                        else:
                            count7 += 1
                    elif y > y4[0] and y < y4[1]:
                        if w > mw and h <= mh:
                            count_in_area = int(w / mw) + 1
                            count8 += count_in_area
                        elif h > mh and w <= mw:
                            count_in_area = int(h / mh) + 1
                            count8 += count_in_area
                        elif h > mh and w > mw:
                            count_in_area1 = int(h / mh) + 1
                            count_in_area2 = int(w / mw) + 1
                            count_in_area = count_in_area1 * count_in_area2
                            count8 += count_in_area
                        else:
                            count8 += 1
            cv2.drawContours(resize, ccs, -1, (0, 255, 0), 3)
            cv2.imshow("Counting...", resize)
            # cv2.imwrite(str(i) + ".jpg", resize)
        if i % 11 == 0:    
            offset = 76
            y1 = [0, 0 + offset]
            y2 = [200, 200 + 3 + offset]
            y3 = [400, 400 + 34 + offset]
            y4 = [600, 600 + 40 + offset]
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            # resize = cv2.resize(frame, (int(frame.shape[1]/rate), int(frame.shape[0]/rate)))  # resize the frame
            resize = cv2.resize(frame, resolution)
            gray = cv2.cvtColor(resize, cv2.COLOR_BGR2GRAY)
            # cv2.imshow('frame',gray)
            (thresh, sure_fg, sure_bg) = img_preprocessing(gray)
            sure_bg = 255 - sure_bg
            contours, hierarchy = cv2.findContours(
                    sure_bg, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            # if i == 220:
            for c in contours:
                x, y, w, h = cv2.boundingRect(c)
                # if w < int(frame.shape[1]/rate) and h < int(frame.shape[0]/rate):
                if w < 50 and h < 50:
                    # print(w, h)
                    # img = cv2.rectangle(sure_bg, (x, y), (x+w, y+h),(0, 255, 0), 5)
                    # cv2.imshow("rect", img)
                    # cv2.waitKey(0)
                    if y > y1[0] and y < y1[1]:
                        if w > mw and h <= mh:
                            count_in_area = int(w / mw) + 1
                            count9 += count_in_area
                        elif h > mh and w <= mw:
                            count_in_area = int(h / mh) + 1
                            count9 += count_in_area
                        elif h > mh and w > mw:
                            count_in_area1 = int(h / mh) + 1
                            count_in_area2 = int(w / mw) + 1
                            count_in_area = count_in_area1 * count_in_area2
                            count9 += count_in_area
                        else:
                            count9 += 1
                    elif y > y2[0] and y < y2[1]:
                        if w > mw and h <= mh:
                            count_in_area = int(w / mw) + 1
                            count10 += count_in_area
                        elif h > mh and w <= mw:
                            count_in_area = int(h / mh) + 1
                            count10 += count_in_area
                        elif h > mh and w > mw:
                            count_in_area1 = int(h / mh) + 1
                            count_in_area2 = int(w / mw) + 1
                            count_in_area = count_in_area1 * count_in_area2
                            count10 += count_in_area
                        else:
                            count10 += 1
                    elif y > y3[0] and y < y3[1]:
                        if w > mw and h <= mh:
                            count_in_area = int(w / mw) + 1
                            count11 += count_in_area
                        elif h > mh and w <= mw:
                            count_in_area = int(h / mh) + 1
                            count11 += count_in_area
                        elif h > mh and w > mw:
                            count_in_area1 = int(h / mh) + 1
                            count_in_area2 = int(w / mw) + 1
                            count_in_area = count_in_area1 * count_in_area2
                            count11 += count_in_area
                        else:
                            count11 += 1
                    elif y > y4[0] and y < y4[1]:
                        if w > mw and h <= mh:
                            count_in_area = int(w / mw) + 1
                            count12 += count_in_area
                        elif h > mh and w <= mw:
                            count_in_area = int(h / mh) + 1
                            count12 += count_in_area
                        elif h > mh and w > mw:
                            count_in_area1 = int(h / mh) + 1
                            count_in_area2 = int(w / mw) + 1
                            count_in_area = count_in_area1 * count_in_area2
                            count12 += count_in_area
                        else:
                            count12 += 1
        i += 1
    # counts = [count1, count2, count3, count4, count5, count6, count7, count8, count9, count10, count11, count12]
    counts = [count1, count2, count3, count5, count6, count7, count9, count10, count11]
    counts_9 = [count1, count2, count3]
    counts_10 = [count5, count6, count7]
    counts_11 = [count9, count10, count11]
    result = int(statistics.mean(counts))
    result = '{"count": "' + str(result) +'"}';
    print (result)
    sys.stdout.flush()

if __name__ == '__main__':
    main()
