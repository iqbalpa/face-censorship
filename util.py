import cv2

def draw_box(img, facial_area):
  cv2.rectangle(
    img,
    (facial_area[2], facial_area[3]), # top-left corner
    (facial_area[0], facial_area[1]), # bottom-right corner
    (0, 0, 255),
    -1
  )

def blur_face(img, facial_area):
  top_left = (facial_area[2], facial_area[3])
  bottom_right = (facial_area[0], facial_area[1])
  x,y = top_left[0], top_left[1]
  w, h = bottom_right[0] - top_left[0], bottom_right[1] - top_left[1]
  # region of interest
  ROI = img[y:y+h, x:x+w]
  blur = cv2.GaussianBlur(ROI, (51, 51), 0)
  # put back ROI into image
  img[y:y+h, x:w+h] = blur
  return img