from retinaface import RetinaFace
import cv2
import util

# Process Video
def censor_video(input_path: str, output_path: str):
  cap = cv2.VideoCapture(input_path)
  
  # if failed to open the video, return immediately
  if not cap.isOpened():
    return
  
  # Get video info
  fps = cap.get(cv2.CAP_PROP_FPS)
  width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
  height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

  # Create output writer
  fourcc = cv2.VideoWriter_fourcc(*'mp4v')
  out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

  # Frame-by-frame processing
  while True:
      ret, frame = cap.read()
      if not ret:
          break

      # Detect faces
      faces = RetinaFace.detect_faces(frame)
      if isinstance(faces, dict):
          for key in faces:
              util.draw_box(frame, faces[key]['facial_area'])

      # Write modified frame
      out.write(frame)

  # Release resources
  cap.release()
  out.release()