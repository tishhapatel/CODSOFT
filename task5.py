import cv2
import matplotlib.pyplot as plt

# Load the pre-trained Haar Cascade classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Load the image in which you want to detect faces
img = cv2.imread("C:/Users/TISHA/Downloads/th (1).jpeg")

# Convert the image to grayscale (necessary for Haar Cascade to work)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Draw rectangles around the detected faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

# Convert the BGR image (default in OpenCV) to RGB for displaying
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Display the image with detected faces using matplotlib
plt.imshow(img_rgb)
plt.axis('off')  # Hide axes
plt.show()
