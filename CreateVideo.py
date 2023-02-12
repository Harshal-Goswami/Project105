import os
import cv2

vid = cv2.VideoCapture[0]

path = "Images"
images = []



if(vid.isOpened()==False):
    print("Unable to see Video")

height = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(height)
width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
print(width)
fps = int(vid.get(cv2.CAP_PROP_FPS))
print(fps)

for file in os.dir(path):
    name, ext = os.path.slitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg', '.jfif']:
        file_name = path+'/'+file

        print(file_name)

        images.append(file_name)

print(len(images))
count = len(images)

frame = cv2.imread(images[0])
height, width, channels = frame.shape
size = width. height
print(size)

for i in range(count-1,0,count-1):
    frame = cv2.imread(images[i])
    out.write(frame)

out.release()
print("Done")

out = cv2.VideoWriter()

while True():
    ret, frame = vid.read()

    cv2.imshow("Web Cam", frame)
    out.Write(frame)
    
    if cv2.waitKey(25) == 32:
        break

vid.release()
out.release()

cv2.destroyAllWindows()