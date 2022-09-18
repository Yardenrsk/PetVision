import cv2
from YOLOv6.YOLOv6 import YOLOv6
from YOLOv6.utils import class_names
import pygame
import time

def toggle_sound(new_state):
    '''
    Toggles sound on and off based on the current state of pet on couch
    :param new_state: representing if there's a pet on the couch currently
    '''
    if new_state:
        pygame.mixer.music.load("DATA/down.mp3")
        pygame.mixer.music.play(loops=-1)
        inner_flag = new_state
    else:
        pygame.mixer.music.stop()

def detect_pets_on_couches(img):
    '''
    Detects all the pets and couches in a frame and drawing boxes around them.
    Also, checking if pets are on the couches or not.
    :param img: the image/frame to detect
    :return: an edited image with boxes around the obojects, and a boolean representing if there are pets on the couches.
    '''
    boxes, scores, class_ids = yolov6_detector(img)
    edited_img = yolov6_detector.draw_detections(img)
    pet_on_couch = False
    pets = []
    couches = []
    for box, score, class_id in zip(boxes, scores, class_ids):
       #creating lists of pets and couches to detect overlapings
        if (class_names[class_id] in ['dog', 'cat']):
            pets.append(box)
        elif (class_names[class_id] in ['couch', 'sofa']):
            couches.append(box)
    for couch_box in couches:
        if not pet_on_couch:
            for pet_box in pets:
                couch_x1, couch_y1, couch_x2, couch_y2 = couch_box.astype(int)
                pet_x1, pet_y1, pet_x2, pet_y2 = pet_box.astype(int)
                #checking if the pet is on the couch (the pet might be higher than the couch's box or standing by the couch)
                if (couch_x1 <= pet_x1 and couch_x2 >= pet_x2
                        and couch_y2-(couch_y2-couch_y1)//8 >= pet_y2 and couch_y1 <= pet_y2):
                    pet_on_couch = True
                    break
    if pet_on_couch:
        img_height, img_width = edited_img.shape[:2]
        font_size = min([img_height, img_width]) * 0.003
        text_thickness = int(min([img_height, img_width]) * 0.008)
        (tw, th), _ = cv2.getTextSize(text="DETECTED PETS ON THE COUCH!", fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                                      fontScale=font_size, thickness=text_thickness)
        edited_img =  cv2.putText(edited_img, "DETECTED PETS ON THE COUCH!", ((img_width-tw)//2,img_height-th),
                        cv2.FONT_HERSHEY_SIMPLEX, font_size, (0, 0, 255), text_thickness, cv2.LINE_AA)
    return edited_img, pet_on_couch


def detect_video_file():
    '''
    Video detection from a file (developed on mac osx, for windows users - use 'VIDX' instead of 'XVID' on line 65)
    '''
    cap = cv2.VideoCapture("DATA/EXAMPLES/TESTS/test.mp4")
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    out = cv2.VideoWriter('DATA/EXAMPLES/RESULTS/output2.mp4', cv2.VideoWriter_fourcc(*'XVID'), 25, (width, height))
    cv2.namedWindow("Detected Objects", cv2.WINDOW_NORMAL)
    state = False
    while cap.isOpened():

        # Press key q to stop
        if cv2.waitKey(1) == ord('q'):
            break

        try:
            # Read frame from the video
            ret, frame = cap.read()
            if not ret:
                break
        except Exception as e:
            print(e)
            continue

        # Update object localizer
        edited_img, new_state = detect_pets_on_couches(frame)
        cv2.imshow("Detected Objects", edited_img)
        if state != new_state:
            toggle_sound(new_state)
            state = new_state

        out.write(edited_img)

    out.release()

def detect_webcam():
    '''
    Video detection from a webcam
    '''
    cap = cv2.VideoCapture(0)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    cv2.namedWindow("Detected Objects", cv2.WINDOW_NORMAL)
    state = False
    while cap.isOpened():

        # Press key q to stop
        if cv2.waitKey(1) == ord('q'):
            break

        try:
            # Read frame from the video
            ret, frame = cap.read()
            if not ret:
                break
        except Exception as e:
            print(e)
            continue

        # Update object localizer
        edited_img, new_state = detect_pets_on_couches(frame)
        cv2.imshow("Detected Objects", edited_img)
        if state != new_state:
            toggle_sound(new_state)
            state = new_state

if __name__ =="__main__":
    model_path = "models/yolov6s.onnx"
    yolov6_detector = YOLOv6(model_path, conf_thres=0.5, iou_thres=0.5)
    pygame.mixer.init()
    # detect_video()
    detect_webcam()