import cv2, time

first_frame = None

video = cv2.VideoCapture(0)

while True:
    check, frame = video.read()
    current_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    current_frame = cv2.GaussianBlur(current_frame, (21, 21), 0)
    if first_frame is None:
        first_frame = current_frame
        continue

    delta_frame = cv2.absdiff(first_frame, current_frame)
    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)

    (cnts, _) = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in cnts:
        if cv2.contourArea(contour) < 1000:
            continue
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

    cv2.imshow("Capturing", current_frame)
    cv2.imshow("Capturing delta", delta_frame)
    cv2.imshow("Capturing threshold", thresh_frame)
    cv2.imshow("Capturing frame", frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
