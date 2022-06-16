import cv2
import time

class Video:
    def __init__(self):
        self.cam = cv2.VideoCapture(0)
        self.pps = 6
        self.dur = 1

    def take_picture(self, img_counter):
        ret, frame = self.cam.read()
        if ret:
            img_name = "opencv_frame_{}.png".format(img_counter)
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            img_counter += 1
        else:
            print("failed to grab frame")

    def capture_video(self):
        for i in range(self.pps*self.dur):
            self.take_picture(i)
            time.sleep(1/self.pps)

        self.cam.release()
