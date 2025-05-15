from retinaface import RetinaFace
import cv2
import util

# Process Image
def censor_image(input_path: str, output_path: str):
  img = cv2.imread(input_path)
  obj = RetinaFace.detect_faces(input_path)

  # draw the red box
  for key in obj.keys():
    identity = obj[key]
    facial_area = identity['facial_area']
    util.draw_box(img, facial_area)
  
  # save the image
  cv2.imwrite(output_path, img)