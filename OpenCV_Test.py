import cv2

cap = cv2.VideoCapture('Test3.mp4')
if (cap.isOpened()== False):
  print("Error opening video stream or file")
i = 0
threshold = 15
while (cap.isOpened()):
    ret, currentFrame = cap.read()
    if ret == True:
        
        if (i > 0):
            currentGray = cv2.cvtColor(currentFrame, cv2.COLOR_BGR2GRAY)
            oldGray = cv2.cvtColor(oldFrame, cv2.COLOR_BGR2GRAY)
            gray_mask = cv2.subtract(currentGray, oldGray)

            
            

            retval, mask_thresh = cv2.threshold( gray_mask, threshold, 255, cv2.THRESH_BINARY)
            kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
            mask_eroded = cv2.morphologyEx(mask_thresh, cv2.MORPH_OPEN, kernel)

            contours, hierarchy = cv2.findContours(mask_eroded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
         
            min_contour_area = 50
            large_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > min_contour_area]

            outFrame = currentFrame.copy()
            for cnt in large_contours:
                x, y, w, h = cv2.boundingRect(cnt)
                outFrame = cv2.rectangle(outFrame, (x, y), (x+w, y+h), (0, 0, 200), 3)
            
            cv2.imshow('Frame', outFrame)
            
        oldFrame = currentFrame
        i = 1
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
