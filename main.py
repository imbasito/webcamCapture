from webcam import WebCamera

camera = WebCamera()

while True:
    frame = camera.capture_and_show_frame()
    if frame is None:
        break
    key = camera.check_key_press()

    if key == 'ESC':
        break
    elif key == 'SPACE':
        camera.save_frame(frame)
    
    if camera.check_window_closed():
        break

camera.release_camera()

