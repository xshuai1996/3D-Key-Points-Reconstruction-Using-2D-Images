import cv2
from glob import glob

img_pattern = './HW3_data/rdimage.???.ppm'

for idx, this_path in enumerate(sorted(glob(img_pattern))):
    this_img = cv2.imread(this_path)
    cv2.imwrite('./output/'+str(idx)+'.jpg', this_img)
