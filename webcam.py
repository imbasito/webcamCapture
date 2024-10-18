import cv2

class WebCamera:
    def __init__(self):
        self.cam = cv2.VideoCapture(0)
        cv2.namedWindow("Web Camera")
        self.img_counter = 0

    def capture_and_show_frame(self):
        ret, frame = self.cam.read()
        if not ret:
            print("failed to grab frame")
            return None
        cv2.imshow("Web Camera", frame)
        return frame

    def check_key_press(self):
        k = cv2.waitKey(1)
        if k % 256 == 27:  # ESC pressed
            print("Escape hit, closing...")
            return 'ESC'
        elif k % 256 == 32:  # SPACE pressed
            return 'SPACE'
        return None

    def save_frame(self, frame):
        img_name = "frame_{}.png".format(self.img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        self.img_counter += 1

    def check_window_closed(self):
        if cv2.getWindowProperty("Web Camera", cv2.WND_PROP_VISIBLE) < 1:
            print("Window close button hit, closing...")
            return True
        return False

    def release_camera(self):
        self.cam.release()
        cv2.destroyAllWindows()
