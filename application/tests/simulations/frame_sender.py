import json
from http import client
from time import time
import numpy as np

import cv2
import requests

video_capture = cv2.VideoCapture(0)

host = "127.0.0.1"
port = '5000'
url = "/api/1.0/frames"

con = client.HTTPConnection(host, port)
con.connect()

try:
    while True:

        # Grab a single frame of video
        ret, frame = video_capture.read()

        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # frame = frame[:, :, ::-1]
        rgb_image = small_frame[:, :, ::-1]

        cv2.imshow('Video', frame)

        t0 = time()
        r = requests.post(f"http://{host}:{port}" + url, json={"frame": rgb_image.tolist()})

        response = r.content
        print(response)
        print()
        #print("time ", time() - t0)

        # Hit 'q' on the keyboard to quit!
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        # time.sleep(3)
finally:
    con.close()
    video_capture.release()
    cv2.destroyAllWindows()
