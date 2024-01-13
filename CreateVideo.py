import os
import cv2

path = "Images/"

images = []

for file in os.listdir(path):
    name, extension = os.path.splitext(file)
    if extension.lower() in ['.jpg', '.jpeg', '.png', '.gif']:
        file_name = path+'/'+file
        print(file_name)
        images.append(file_name)

count = len(images)

if count == 0:
    print("No images found in the specified folder.")
else:
    frame = cv2.imread(images[0])
    height, width, channels = frame.shape
    size = (width, height)
    print(size)

    out = cv2.VideoWriter('Project.avi', cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)

    for i in range(0,count):
        img = cv2.imread(images[i])
        
        if img is not None:
            out.write(img)
        else:
            print(f"Error reading image: {images[i]}")

    out.release()

    print("Done")
