import cv2
from djitellopy import Tello
from droneblocks.DroneBlocksTello import DroneBlocksTello
import time
from threading import Thread
from datetime import datetime

dbtello = DroneBlocksTello()
# Initialize Tello
tello = Tello()
tello.connect()
# Set up video capture
tello.streamon()
cap = tello.get_frame_read()
time.sleep(2)

dbtello.clear_everything()
scrolling_text = "Hello!!!"
dbtello.scroll_string(message=scrolling_text,
                      scroll_dir=DroneBlocksTello.LEFT,
                      display_color=DroneBlocksTello.RED,
                      rate=2.5)


keepRecording = True

battery = tello.get_battery()
if battery <= 20:
    print("[WARNING]: Battery is low.", battery, "%")
else:
    print("Battery: ", battery, "%")


# Start flying
tello.takeoff()
time.sleep(2)
 # Move up by 30 cm initially
tello.move_up(70)
for i in range(6):
    tello.rotate_clockwise(60)


dbtello.clear_everything()
# ArUco dictionary and parameters
aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_ARUCO_ORIGINAL)
aruco_params = cv2.aruco.DetectorParameters_create()

def videoRecorder():
    # create a VideoWrite object, recoring to ./video.avi
    height, width, _ = cap.frame.shape
    video_file = f"video_{datetime.now().strftime('%d-%m-%Y_%I-%M-%S_%p')}.mp4"
    video = cv2.VideoWriter(video_file, cv2.VideoWriter_fourcc(*'XVID'), 30, (width, height))

    while keepRecording:
        video.write(cap.frame)
        time.sleep(1 / 30)

    video.release()

recorder = Thread(target=videoRecorder)

while True:
    # Read frame from video capture
    frame = cap.frame

    # Detect ArUco markers
    corners, ids, rejected = cv2.aruco.detectMarkers(frame, aruco_dict, parameters=aruco_params)

    if ids is not None:
        # Draw marker boundaries and IDs
        recorder.start()
        cv2.aruco.drawDetectedMarkers(frame, corners, ids)
        print("Marker detected")
        dbtello.display_smile(display_color=DroneBlocksTello.BLUE)
        tello.move_up(40)
        time.sleep(2)
        #tello.move_down(50)
        #time.sleep(1)
        for i in range(12):
            tello.rotate_clockwise(30)
            time.sleep(1)
        tello.land()
        keepRecording = False
        recorder.join()
    else:
        tello.rotate_clockwise(30)
        print("Marker Not detected")
        dbtello.display_sad(display_color=DroneBlocksTello.BLUE)
        time.sleep(3)
    # Display frame
    cv2.imshow('ArUco Marker Detection', frame)

    # Break loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video capture and close windows
tello.streamoff()
tello.land()
cv2.destroyAllWindows()