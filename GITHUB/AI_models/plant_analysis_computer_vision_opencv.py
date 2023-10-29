import cv2
import numpy as np
import time

def thermal_analysis(img):
    return cv2.applyColorMap(img, cv2.COLORMAP_JET)

start = time.time()

img = cv2.imread(path_to_image)
img = cv2.resize(img, (250, 250))
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

range1, range2 = (26, 0, 0), (86, 255, 255)
mask1 = cv2.inRange(hsv, range1, range2)
kernel1 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
mask2 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, kernel1)
mask2 = cv2.morphologyEx(mask1, cv2.MORPH_CLOSE, kernel1)
res = cv2.bitwise_and(img, img, mask=mask2)

range1, range2 = (38, 0, 0), (86, 255, 255)
mask = cv2.inRange(hsv, range1, range2)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
t = mask
mask = cv2.merge([mask, mask, mask])
mask_inv = 255 - mask
white = np.full_like(img, (255, 255, 255))
img_masked = cv2.bitwise_and(img, mask)
white_masked = cv2.bitwise_and(white, mask_inv)
result = cv2.add(img_masked, mask_inv)

thermal_img = thermal_analysis(img)

x = cv2.countNonZero(t)
y = cv2.countNonZero(mask2)

severity = 1 - (x/y)

print(x, y)
print(f"Severity of disease is {severity:.2f}")

if severity > 0.1:
    print("The plant has a disease.")
elif severity > 0.7:
    print("The plant has a lots of diseases!!")
else:
    print("The plant is healthy.")

canvas = np.ones((250, 5*250, 3), dtype=np.uint8) * 255

canvas[0:250, 0:250] = img
canvas[0:250, 250:500] = hsv
canvas[0:250, 500:750] = thermal_img
canvas[0:250, 750:1000] = result
canvas[0:250, 1000:1250] = cv2.cvtColor(mask1, cv2.COLOR_GRAY2BGR)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(canvas, 'Original', (10, 240), font, 0.75, (255, 0, 0), 2, cv2.LINE_AA)
cv2.putText(canvas, 'HSV', (260, 240), font, 0.75, (255, 0, 0), 2, cv2.LINE_AA)
cv2.putText(canvas, 'Thermal', (510, 240), font, 0.75, (255, 0, 0), 2, cv2.LINE_AA)
cv2.putText(canvas, 'Result', (760, 240), font, 0.75, (255, 0, 0), 2, cv2.LINE_AA)
cv2.putText(canvas, 'Binary', (1010, 240), font, 0.75, (255, 0, 0), 2, cv2.LINE_AA)

end = time.time()
print(f"Runtime of the program is {end - start:.2f} seconds")

cv2.imshow("Original Image", img)
cv2.imshow("HSV Image", hsv)
cv2.imshow("Thermal Image", thermal_img)
cv2.imshow("Result Image", result)
cv2.imshow("Binary Image", mask1)
cv2.imshow("Analysis Overview", canvas)

cv2.waitKey(0)
cv2.destroyAllWindows()
