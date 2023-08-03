import os.path
import concurrent.futures.thread

import numpy as np

from person_identification import face_recognition_main as face
# from ball_tracker import sequence_liveness_main as seq
import cv2
from fastapi import FastAPI, File, UploadFile, Form, UploadFile, Response
from fastapi.responses import FileResponse


def face_identification():
    counter = 0
    result = ""
    img = cv2.imread(os.path.join("photos", "sample_1.jpeg"))
    # cap = cv2.VideoCapture(os.path.join("photos", "video_1.mp4"))
    # cap.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
    # cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 640)
    print(face.recognize(os.path.join("photos", "video_1.mp4"), img))
    # while not cap.isOpened():
    #     print("camera open failed")
    #     cap = cv2.VideoCapture(os.path.join("photos", "video_1.mp4"))
    #     cv2.waitKey(1000)
    # while cap.isOpened():
    #     ret, frame = cap.read()
    #     cv2.flip(frame, 1)
    #     if ret:
    #         if counter % 10 == 0:
    #             try:
    #                 with concurrent.futures.ThreadPoolExecutor() as executor:
    #                     future = executor.submit(face.recognize, frame, img)
    #                     result = future.result()
    #             except ValueError:
    #                 pass
    #         counter += 1
    #         if result == 'face_match':
    #             cv2.putText(frame, "Wajah sama", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
    #         elif result == 'face_not_match':
    #             cv2.putText(frame, "Wajah tidak sama", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
    #     cv2.imshow("Result", frame)
    #     if cap.get(cv2.CAP_PROP_POS_FRAMES) >= cap.get(cv2.CAP_PROP_FRAME_COUNT):
    #         break
    #     key = cv2.waitKey(20)
    #     if key == ord("q"):
    #         break
    # cv2.destroyAllWindows()


def sequence():
    LEFT_EYE = [362,382,381,380,374,373,390,249, 263, 466, 388, 387, 386, 385, 384, 398]
    LEFT_IRIS = [474, 475, 476, 477]
    RIGHT_EYE = [33, 7, 163, 144, 145, 153, 154, 155, 133, 173, 157, 158, 159, 160, 161, 246]
    RIGHT_IRIS = [469, 470, 471, 472]
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 640)
    while True:
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        # mesh_points = seq.predict(frame)
        # if len(mesh_points) != 0:
        #     (l_cx, l_cy), l_radius = cv2.minEnclosingCircle(mesh_points[LEFT_IRIS])
        #     (r_cx, r_cy), r_radius = cv2.minEnclosingCircle(mesh_points[RIGHT_IRIS])
        #     center_left = np.array([l_cx, l_cy], dtype=np.int32)
        #     center_right = np.array([r_cx, r_cy], dtype=np.int32)
        #     cv2.circle(frame, center_left, int(l_radius), (0,255,0), 1, cv2.LINE_AA)
        #     cv2.circle(frame, center_right, int(r_radius), (0, 255, 0), 1, cv2.LINE_AA)
        #     cv2.polylines(frame, [mesh_points[LEFT_EYE]], True, (0,255,0), 1, cv2.LINE_AA)
        #     cv2.polylines(frame, [mesh_points[RIGHT_EYE]], True, (0, 255, 0), 1, cv2.LINE_AA)
        # cv2.imshow("Result", frame)
        key = cv2.waitKey(1)
        if key == ord("q"):
            break
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    # sequence()
    face_identification()
    # print(cv2.__version__)
