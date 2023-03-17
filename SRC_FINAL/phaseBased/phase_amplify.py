import cv2
import numpy as np

def phaseAmplify(vidFile):
    # magPhase , fl, fh,fs, outDir, varargin
    # Read the video

    cap = cv2.VideoCapture(vidFile)
    videoBuffer = 0

    while cap.isOpened():
        ret, frame = cap.read()


        if ret:
            cv2.imshow("frame", frame)
            if type(videoBuffer) == int:
                videoBuffer = np.array([frame])

            else:
                videoBuffer = np.concatenate((videoBuffer, [frame]))

            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        else:
            break
    cap.release()
    cv2.destroyAllWindows()

    return videoBuffer

videoBuffer = phaseAmplify("../../../data/car_engine.avi")
print(videoBuffer.shape)
