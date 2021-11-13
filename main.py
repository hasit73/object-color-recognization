from yolo import YoloDetection
import cv2
import argparse
import color_identification
import time 

CONFIG_FILE = None
model = None

def load_config(config_path):
    global CONFIG_FILE
    CONFIG_FILE = eval(open(config_path).read())


def load_model():
    global model
    model = YoloDetection(CONFIG_FILE["model-parameters"]["model-weights"],
                    CONFIG_FILE["model-parameters"]["model-config"],
                    CONFIG_FILE["model-parameters"]["model-names"],
                    CONFIG_FILE["shape"][0],
                    CONFIG_FILE["shape"][1])


def start_detection(media_path):
    cv2.namedWindow("Video",cv2.WINDOW_NORMAL)
    cap = cv2.VideoCapture(media_path)
    ret = True
    while ret:
        ret , frame = cap.read()
        if(ret):
            start_time = time.time()
            detections = model.process_frame(frame)
            for o in detections:
                class_name = o[0]
                x,y,w,h = o[1:5]
                cut_image = frame[y:y+h , x:x+w]
                color = color_identification.getcolor(cut_image)
                text = class_name+"-"+color
                cv2.rectangle(frame,(x, y), (x + w, y + h), (255, 0, 0), 3)
                cv2.rectangle(frame,(x,y-20),(x+80,y),thickness=-1,color=(255,0,0))
                cv2.putText(frame,text,(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 2)
            end_time = time.time()
            fps = round(1/(end_time-start_time) , 2)
            cv2.putText(frame,f"FPS : {fps}",(50,50),cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 2)
            
            cv2.imshow("Video",frame)
            key = cv2.waitKey(30)
            
            ## quit detection when esc key pressed
            if(key==27):
                break

            ## paused detection when space key pressed
            if(key==32):
                cv2.waitKey(-1)

    cv2.destroyAllWindows()

if __name__=="__main__":
    parser = argparse.ArgumentParser(description="Provide arguements")
    parser.add_argument("--config","-c")
    parser.add_argument("--debug","-d")
    parser.add_argument("--video","-v")    
    args = parser.parse_args()
    config_path = args.config
    load_config(config_path)
    load_model()
    start_detection(args.video)


