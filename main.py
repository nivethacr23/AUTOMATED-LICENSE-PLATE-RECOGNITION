import cv2

# Load the pre-trained Haar cascade for license plate detection
plate_cascade = cv2.CascadeClassifier("haarcascade_russian_plate_number.xml")

# Load the image (replace with your own image path)
image = cv2.imread('car.jpg')  # Make sure this image is in the same folder
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect plates
plates = plate_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

# Draw rectangles around detected plates
for (x, y, w, h) in plates:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    plate_roi = image[y:y + h, x:x + w]
    cv2.imshow('Detected Plate', plate_roi)

cv2.imshow('Vehicle Image with Plate', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
