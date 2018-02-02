#################
#PHOTOBOOTH FILE#
#################
import cv2
from datetime import datetime
from pathlib import Path
import os


def run():
    import cv2
    from datetime import datetime
    from pathlib import Path
    import os

    camera = cv2.VideoCapture(0)

    while (True):
        try:
            return_value, image = camera.read()

            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            homeDir = str(Path.home())
            pictureDir = homeDir + "/Pictures/gitPics"
            if not os.path.isdir(pictureDir):
                os.makedirs(pictureDir)
            now = datetime.now()
            name = '{h}/capture-{t.year}-{t.month}-{t.day}_{t.hour}-{t.minute}-{t.second}.jpg'.format(h=pictureDir,
                                                                                                      t=now)
            print("saving ", name)
            cv2.imwrite(name, image)
            break
        except:
            print("exiting...")
            break

    camera.release()
    cv2.destroyAllWindows()