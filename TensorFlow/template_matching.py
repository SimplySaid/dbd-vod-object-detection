import cv2
import os

#imread
#imshow
#waitkey
#VideoCapture

#dirname = os.path.dirname(__file__)

BASE_W, BASE_H = 2560, 1440
TEMPLATE_SCALED_W, TEMPLATE_SCALED_H = 0, 0

#Load Images
base_img = cv2.imread('input/base.png', 0)
#template = cv2.imread('input/icons/iconPerks_DeadHard.jpg', 0)
template = cv2.imread('input/icons/ds_test.png', 0)

#Resize Template
template = cv2.resize(template, (0,0), fx=0.90, fy=0.90) 

h, w = template.shape

# template = cv2.cvtColor(template, cv2.COLOR_BGR2RGB)

# cv2.imshow('base', base_img)
# cv2.imshow('template', template)

methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
            cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

for method in methods:
    img2 = base_img.copy()

    result = cv2.matchTemplate(img2, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc

    bottom_right = (location[0] + w, location[1] + h)    
    cv2.rectangle(img2, location, bottom_right, 255, 5)
    cv2.imshow('Match', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
