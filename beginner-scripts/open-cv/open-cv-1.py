import cv2

print(cv2.__version__)


camSlot = 0 # CSI MIPI
width = 800
height = 600
flipMethod = 2 # CSI MIPI 0- Don't flip, 2 = flip vertically
#camSet = f'nvarguscamerasrc sensor-id={camSlot} ! video/x-raw(memory:NVMM), width=3264, height=2464 framerate=21/1, format=NV12 ! nvvidconv flip-method={flipMethod} video/x-raw, width={width}, height={height}, format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink' # CSI MIPI
camSet = f'v4l2src device=/dev/video{camSlot} ! video/x-raw, width={width}, height={height}, framerate=24/1 ! videoconvert ! appsink'
#cam = cv2.VideoCapture(f'/dev/video{camSlot}')
cam = cv2.VideoCapture(camSet)

while True:
  _, frame = cam.read()
  # Magic happens here
  cv2.imshow('My Cam', frame)
  cv2.moveWindow('My Cam', 0, 0)
  if cv2.waitKey(1) == ord('q'):
    break

cam.release()
cv2.destroyAllWindows()
