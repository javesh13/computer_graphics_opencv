import cv2
import matplotlib as plt
import numpy as np

canvas_height = 640
canvas_width = 480

canvas = np.zeros([canvas_width, canvas_height, 3], np.uint8)
canvas.fill(255)


color = [0, 0, 255]

center_x = int(input("Enter center x coordinate: "))
center_y = int(input("Enter center y coordinate: "))
r = int(input("Enter radius: "))

print("Press any key to close the window ")

d = 3 - 2 * r;
x = 0
y = r

while(y >= x):
    
    canvas[int(center_x + x)][int(center_y + y)] = color
    canvas[int(center_x - x)][int(center_y + y)] = color
    canvas[int(center_x + x)][int(center_y - y)] = color
    canvas[int(center_x - x)][int(center_y - y)] = color
    canvas[int(center_x + y)][int(center_y + x)] = color
    canvas[int(center_x - y)][int(center_y + x)] = color
    canvas[int(center_x + y)][int(center_y - x)] = color
    canvas[int(center_x - y)][int(center_y - x)] = color

    x += 1
    if(d > 0):
        y -= 1
        d = d + 4 * (x - y) + 10;
    else:
        d = d + 4 * x + 6
    
    canvas[int(center_x + x)][int(center_y + y)] = color
    canvas[int(center_x - x)][int(center_y + y)] = color
    canvas[int(center_x + x)][int(center_y - y)] = color
    canvas[int(center_x - x)][int(center_y - y)] = color
    canvas[int(center_x + y)][int(center_y + x)] = color
    canvas[int(center_x - y)][int(center_y + x)] = color
    canvas[int(center_x + y)][int(center_y - x)] = color
    canvas[int(center_x - y)][int(center_y - x)] = color


    cv2.imshow("my_window", canvas)
    cv2.waitKey(40)

cv2.waitKey(0)
cv2.destroyAllWindows()
