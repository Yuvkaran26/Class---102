import cv2
import time
import random
import dropbox

stat_time = time.time()
# print(stat_time)

def takepic():
    number = random.randint(1,100)
    video = cv2.VideoCapture(0)
    time.sleep(3)
    dummy,frame=video.read()
    print(dummy)
    if dummy == True:
        imageName = "image"+str(number)+".png"
        cv2.imwrite(imageName, frame)
        stat_time = time.time()
        return imageName
    else:    
        cv2.waitKey(0)
        video.release()
        cv2.destroyAllWindows()

def upload(imageName):
    myToken = "sl.BAQPRnXqzj8QHDUw2uLSbG08GstU2xFsNI1ZcSWMis0DRAidPZnddtvTsrWnz5UZamDMWEjYtNL59LSe9L_FVINT-vAKLfvbiANuNtrrkdmfGsEhulEV3BHTDPZEgU-8uJ7ko5Y"
    filefrom=imageName
    fileTo = "/snapshot/" + imageName
    box = dropbox.Dropbox(myToken)
    f = open(filefrom, "rb")
    box.files_upload(f.read(), fileTo, mode= dropbox.files.WriteMode.overwrite)
    print("file uploaded")


def main():
    while(True):
        if(time.time() - stat_time >= 5):
            name = takepic()
            upload(name)

main()

