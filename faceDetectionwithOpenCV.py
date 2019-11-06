## Face Detection with OpenCV


# Import OpenCV
import cv2


# Loading the cascades
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')


# Face Detector
def face_detector(grayScale, originalFrame):
    faces = face_cascade.detectMultiScale(grayScale, 1.3, 5) # Coordinates of detected faces
    for (x1, y1, w1, h1) in faces: # For loop to iterate over detected faces
        cv2.rectangle(originalFrame,
                      (x1, y1), # Upper Left Corner
                      (x1+w1, y1+h1), # Lower Right Corner
                      (255, 255, 0), 3) # Drawing rectangle over face on Original Frame
        roi_gray = grayScale[y1:y1+h1, x1:x1+w1]
        roi_color = originalFrame[y1:y1+h1, x1:x1+w1]
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 3) # Coordinates of detected eyes
        for (x2, y2, w2, h2) in eyes: # For loop to iterate over detected eyes
            cv2.rectangle(roi_color,
                          (x2, y2), # Upper Left Corner
                          (x2+w2, y2+h2), # Lower Right Corner
                          (255, 0, 0), 1) # Drawing rectangle over eye on Original Frame

        return originalFrame


# Accessing webcam to detect face
video_capture = cv2.VideoCapture(0) 

while True: 
    re, frame = video_capture.read()
    
    if re:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
        canvas = face_detector(gray, frame)
        cv2.imshow('Video', canvas)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release() 
cv2.destroyAllWindows() # We destroy all the windows inside which the images were displayed.

