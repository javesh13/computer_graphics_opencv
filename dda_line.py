import cv2
import matplotlib as plt
import numpy as np

canvas_height = 1024    
canvas_width = 1024

canvas = np.zeros([canvas_height, canvas_width, 3], np.uint8)
canvas.fill(255)


color = [255, 0, 0]

start_x = int(input("Enter start x coordinate: "))
start_y = int(input("Enter start y coordinate: "))

end_x = int(input("Enter end x coordinate: "))
end_y = int(input("Enter end y coordinate: "))

dx = end_x - start_x
dy = end_y - start_y
    
steps = abs(dx) if (abs(dx) > abs(dy) ) else abs(dy)

xinc = dx / float(steps)
yinc = dy / float(steps)
    
x = start_x
y = start_y

print("\n Press any key to close the window (click window first)")
for i in range(steps):
    print("x %d y %d" %(x, y))
    canvas[int(y)][int(x)] = color
    #which color of line u want; do you remember the definition of color? (HINT: RGB)
    x += xinc
    y += yinc
    cv2.imshow("canvas", canvas) #plotting updates
    cv2.waitKey(1) #kind of delay its necessary to show window

cv2.waitKey(0)
        
cv2.destroyAllWindows()















cv2.waitKey(0)
cv2.destroyAllWindows()
