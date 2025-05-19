# AUTOMATED-LICENSE-PLATE-RECOGNITION
This project detects vehicle license plates from images using OpenCV and a pre-trained Haar cascade classifier. It highlights plates by drawing boxes and displays the results. Ideal for beginners, it forms the first step toward building complete Automated License Plate Recognition (ALPR) systems.
Purpose:
The main purpose of this project is to build a basic Automated License Plate Recognition (ALPR) system using image processing techniques. ALPR systems are used to automatically identify vehicle license plates from images or videos, helping reduce manual intervention in transportation, security, and traffic monitoring systems. This project focuses on the detection phase, where the location of the license plate is identified in a vehicle image using a Haar Cascade Classifier provided by OpenCV.

By successfully detecting license plates from static images, this project lays the foundation for more advanced systems that can perform real-time recognition, character extraction (OCR), and vehicle tracking in intelligent transportation systems.

Technologies used:
 The project utilizes the following technologies:

Programming Language:

Python 3 – Easy-to-read, versatile language widely used in machine learning and computer vision applications.

Libraries and Tools:

OpenCV – An open-source computer vision and image processing library used to read images, process them, and perform object detection.

Haar Cascade Classifier – A pre-trained object detection model in XML format, specifically haarcascade_russian_plate_number.xml, used to detect license plates in vehicle images.

IDE / Environment:

Any Python-compatible IDE or code editor (e.g., VS Code, Jupyter Notebook, or PyCharm).

Command-line or terminal for running Python scripts.

Platform:

Compatible with Windows, Linux, or macOS environments where Python and OpenCV can be installed

Library used :
This project uses this Python library:

OpenCV (cv2)
A powerful open-source computer vision and machine learning library.
Used for:

Reading and displaying images

Converting color spaces (BGR to Grayscale)

Detecting license plates using Haar cascade classifiers

Drawing rectangles around detected features

Usage :
This project demonstrates how to detect vehicle license plates from static images using image processing techniques with OpenCV. It is particularly useful for beginners or developers who want to understand the foundational step of an Automated License Plate Recognition (ALPR) system — identifying and extracting the license plate region. By running the script, users can load a vehicle image, process it using a pre-trained Haar cascade classifier, and visually detect and highlight the license plate. This can serve as a starting point for more advanced applications such as real-time surveillance, traffic monitoring, toll automation, and smart parking systems. The project is easy to set up, requiring only Python and OpenCV, and can be expanded to include features like OCR for full plate number recognition.
