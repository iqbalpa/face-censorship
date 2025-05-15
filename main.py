from processor import image
from processor import video

IMAGE_INPUT_PATH = "./input/image.png"
VIDEO_INPUT_PATH = "./input/video.mp4"
IMAGE_OUTPUT_PATH = "./output/image.png"
VIDEO_OUTPUT_PATH = "./output/video.mp4"

if __name__ == "__main__":
  image.censor_image(
    IMAGE_INPUT_PATH,
    IMAGE_OUTPUT_PATH
  )
  video.censor_video(
    VIDEO_INPUT_PATH,
    VIDEO_OUTPUT_PATH
  )
