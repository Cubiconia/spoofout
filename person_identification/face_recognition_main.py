import cv2
from deepface import DeepFace

import person_identification.liveness_detection.test as test
from os.path import dirname, join


def recognize(video_path: str, known_image):
    cap = cv2.VideoCapture(video_path)
    cap.get(cv2.CAP_PROP_POS_FRAMES)
    total_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)

    counter = 0
    false_counter = 0
    true_counter = 0
    threshold = 0.1
    known_image = cv2.imread(known_image)
    if total_frames > 150:
        return "video_too_long"
    while not cap.isOpened():
        print("camera open failed")
        cap = cv2.VideoCapture(video_path)
        cv2.waitKey(1000)
    while cap.isOpened():
        ret, frame = cap.read()
        cv2.flip(frame, 1)
        if ret:
            if counter % 15 == 0:
                label, value, image_bbox = test.test(frame.copy(), join(dirname(__file__), "liveness_detection", "resources", "anti_spoof_models"), device_id=0)
                if label == 1:
                    if isMatched(frame, known_image):
                        print("REAL Face", "accuracy:", value)
                        true_counter += 1
                    else:
                        false_counter += 1
                else:
                    print("FAKE Face", "accuracy:", value)
                    false_counter += 1
            counter += 1
        cv2.waitKey(20)
        if cap.get(cv2.CAP_PROP_POS_FRAMES) >= total_frames:
            break
    if false_counter < threshold * (true_counter + false_counter):
        return "face_match"
    else:
        return "face_not_match"


def isMatched(unknown_image_path, known_image_path):
    result = DeepFace.verify(unknown_image_path, known_image_path, model_name="Facenet512",
                             distance_metric="euclidean_l2")
    print("Verified:",result.get('verified'),"Distance:",result.get("distance"),"Threshold:",result.get("threshold"))
    return result.get('verified')
