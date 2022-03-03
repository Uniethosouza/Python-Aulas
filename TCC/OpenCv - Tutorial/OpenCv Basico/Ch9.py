import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier('Python/Advanced Computer Vision with Python/OpenCv Basico/haarcascade_frontalface_default.xml')
# Read the input image
img = cv2.imread('C:/Users/thoma/Desktop/Aprendizado/Python/Advanced Computer Vision with Python/OpenCv Basico/portrait-of-a-man-perhaps-petrus-augustus-de-genestet-1829-1861-unknown-artist-1830-e0126707.jpg')
# Convert into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.3, 3)
# Draw rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 3)
# Display the output
imgResize = cv2.resize(img,(500,500))
cv2.imshow('img', imgResize)
cv2.waitKey()