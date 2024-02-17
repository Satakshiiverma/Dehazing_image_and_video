import cv2
import image_dehazer

image_path='WhatsApp Image 2024-02-10 at 2.15.47 PM.jpeg'
haze_img=cv2.imread(image_path)

haze_corrected_img,haze_map=image_dehazer.remove_haze(haze_img)

cv2.imshow('input image',haze_img)
cv2.imshow('enhanced_image', haze_corrected_img)
cv2.imshow('hazed_map',haze_map)
cv2.waitKey(0)
cv2.destroyAllWindows()

