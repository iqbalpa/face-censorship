import cv2

def draw_box(img, facial_area):
  cv2.rectangle(
    img,
    (facial_area[2], facial_area[3]),
    (facial_area[0], facial_area[1]),
    (0, 0, 255),
    -1
  )
