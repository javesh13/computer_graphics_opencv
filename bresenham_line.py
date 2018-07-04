import cv2
import matplotlib as plt
import numpy as np

canvas_height = 640
canvas_width = 480

canvas = np.zeros([canvas_width, canvas_height, 3], np.uint8)
canvas.fill(255)


color = [255, 0, 0]

start_x = int(input("Enter start x coordinate: "))
start_y = int(input("Enter start y coordinate: "))
end_x = int(input("Enter end x coordinate: "))
end_y = int(input("Enter end y coordinate: "))

m_new = 2 * (end_y - start_y)
slope_error_new = m_new - (end_x - start_x)

x = start_x
y = start_y

print("Press any key to close the window ")
while (x <= end_x and y < end_y):
	print("x %d y%d" %(x, y))
	canvas[int(y)][int(x)] = color
	slope_error_new += m_new

	if(slope_error_new >= 0):
		y += 1
		slope_error_new -= 2 * (end_x - start_x)
	x += 1
	cv2.imshow("my_window", canvas)
	cv2.waitKey(1)


cv2.waitKey(0)
        
cv2.destroyAllWindows()















cv2.waitKey(0)
cv2.destroyAllWindows()
