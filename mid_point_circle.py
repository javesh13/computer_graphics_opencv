import cv2
import matplotlib as plt
import numpy as np

canvas_height = 640
canvas_width = 480

canvas = np.zeros([canvas_width, canvas_height, 3], np.uint8)
canvas.fill(255)


color = [255, 0, 123]

center_x = int(input("Enter center x coordinate: "))
center_y = int(input("Enter center y coordinate: "))
r = int(input("Enter radius: "))

print("Press any key to close the window ")

p = 1 - r
x = r
y = 0

while(x > y):
    y  += 1
    if(p <= 0):
        p = p + 2*y + 1

    else:
        x -= 1
        p = p + 2*y - 2*x + 1

    if( x < y): break


    canvas[int(x + center_x)][int(y + center_y)] = color
    canvas[int(-x + center_x)][int(y + center_y)] = color
    canvas[int(x + center_x)][int(-y + center_y)] = color
    canvas[int(-x + center_x)][int(-y + center_y)] = color


    if(x != y):
        canvas[int(y + center_x)][int(x + center_y)] = color
        canvas[int(-y + center_x)][int(x + center_y)] = color
        canvas[int(y + center_x)][int(-x + center_y)] = color
        canvas[int(-y + center_x)][int(-x + center_y)] = color



    cv2.imshow("my_window", canvas)
    cv2.waitKey(40)
cv2.waitKey(0)
cv2.destroyAllWindows()
