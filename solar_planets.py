import cv2
import numpy as np

img = cv2.imread("solar-system.jpg")

cv2.putText(
    img,
    "sol",
    (100,80),
    fontFace= cv2.FONT_HERSHEY_COMPLEX,
    fontScale= 2,
    color= (0,0,255)
)
cv2.putText(
    img,
    "mercurio",
    (103,270),
    fontFace= cv2.FONT_HERSHEY_COMPLEX,
    fontScale= 0.5,
    color= (0,0,255)
)
cv2.putText(
    img,
    "venus",
    (200,270),
    fontFace= cv2.FONT_HERSHEY_COMPLEX,
    fontScale= 0.5,
    color= (0,0,255)
)
cv2.putText(
    img,
    "terra",
    (300,270),
    fontFace= cv2.FONT_HERSHEY_COMPLEX,
    fontScale= 0.5,
    color= (0,0,255)
)
cv2.putText(
    img,
    "marte",
    (380,270),
    fontFace= cv2.FONT_HERSHEY_COMPLEX,
    fontScale= 0.5,
    color= (0,0,255)
)
cv2.putText(
    img,
    "jupiter",
    (500,370),
    fontFace= cv2.FONT_HERSHEY_COMPLEX,
    fontScale= 0.5,
    color= (0,0,255)
)
cv2.putText(
    img,
    "saturno",
    (700,270),
    fontFace= cv2.FONT_HERSHEY_COMPLEX,
    fontScale= 0.5,
    color= (0,0,255)
)
cv2.putText(
    img,
    "urano",
    (915,270),
    fontFace= cv2.FONT_HERSHEY_COMPLEX,
    fontScale= 0.5,
    color= (0,0,255)
)
cv2.putText(
    img,
    "netuno",
    (1050,270),
    fontFace= cv2.FONT_HERSHEY_COMPLEX,
    fontScale= 0.5,
    color= (0,0,255)
)
cv2.imshow("sistema solar", img)
cv2.waitKey(0)
cv2.imwrite("Solar_systemwithname.jpg",img)
