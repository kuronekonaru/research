import numpy as np
import cv2 as cv
import module.mode_1
import module.mode_2
import module.mode_3

# Main function
def display_help():
    print("EVENT_LBUTTONDOWN is Mode 1")
    print("EVENT_RBUTTONDOWN is Mode 2")
    print("EVENT_MBUTTONDOWN is Mode 3")

# mouse callback function
def select_mode(event,x,y,flags,param):
    if event == cv.EVENT_LBUTTONDOWN:
        #print("Select Mode 1")
        module.mode_1.excute_mode_1()
    elif event == cv.EVENT_RBUTTONDOWN:
        #print("Select Mode 2")
        module.mode_2.excute_mode_2()
    elif event == cv.EVENT_MBUTTONDOWN:
        #print("Select Mode 3")
        module.mode_3.excute_mode_3()

#draw_help
def draw_help(img):

    mode_txt = ["Choose mode!","LBUTTONDOWN is Mode 1","RBUTTONDOWN is Mode 2","MBUTTONDOWN is Mode 3"]
    font = cv.FONT_HERSHEY_PLAIN
    font_size = 2.0
    initial_x=30
    initial_y=30
    step_y=30
	#put txt
    for i in range(len(mode_txt)):
        cv.putText(img,mode_txt[i],(initial_x,initial_y + i * step_y),font, font_size,(255,0,0))
    return img

# Create a black image, a window and bind the function to window
display_help()
menu_img = np.zeros((1024,1024,3), np.uint8)
cv.namedWindow('Menu')
cv.setMouseCallback('Menu',select_mode)
draw_help(menu_img)
cv.imshow('Menu',menu_img)

while(1):
    cv.imshow('Menu',menu_img)
    if cv.waitKey(20) & 0xFF == 27:
        break
cv.destroyAllWindows()
