# -*- coding: utf-8 -*-

import cv2
import numpy as np

# ******* WRITE YOUR FUNCTION, VARIABLES etc HERE


def main(board_filepath, container_filepath):
	'''
This function is the main program which takes image of game-board and
container as argument. Team is expected to insert their part of code as
required to solve the given task (function calls etc).


Function name: main()

Input argument: board_filepath and container_filepath.

Return: 
1 - List of tuples which is the expected final output. See Task1_Description for detail. 
2 - List of tuples for objects on board. See Task1_Description for detail. 
	''' 
        board_objects = []		# List to store output of board -- DO NOT CHANGE VARIABLE NAME
        output_list = []		# List to store final output 	-- DO NOT CHANGE VARIABLE NAME
        position=0
        container_objects = []  
        board_area=[]
        container_area=[]
        shape='none'
        board_shape=["none","none","none","none","none","none","none","none","none"]
        container_shape=["none","none","none","none","none","none","none","none","none","none","none","none","none","none","none","none"]


	##### WRITE YOUR CODE HERE - STARTS

	# cv2.imshow("board_filepath - press Esc to close",cv2.imread(board_filepath))			- For check - remove
	# cv2.imshow("container_filepath - press Esc to close",cv2.imread(container_filepath))

        board=cv2.imread(board_filepath)
        container=cv2.imread(container_filepath)
    
    ##board shapes
        img_hsv = cv2.cvtColor(board, cv2.COLOR_BGR2HSV)

    # lower mask (0-10)
        lower_red = np.array([0,50,50])
        upper_red = np.array([10,255,255])
        mask0 = cv2.inRange(img_hsv, lower_red, upper_red)

    # upper mask (170-180)
        lower_red = np.array([170,50,50])
        upper_red = np.array([180,255,255])
        mask1 = cv2.inRange(img_hsv, lower_red, upper_red)
    #
        lower_blue = np.array([110,50,50])
        upper_blue = np.array([130,255,255])
        mask2 = cv2.inRange(img_hsv, lower_blue, upper_blue)
    #
        lower_green = np.array([50,100,100])
        upper_green = np.array([70,255,255])
        mask3 = cv2.inRange(img_hsv, lower_green, upper_green)
    #
        lower_yellow = np.array([20,240,240]) 
        upper_yellow = np.array([40,255,255])
        mask4 = cv2.inRange(img_hsv, lower_yellow, upper_yellow)
    # join my masks
    #mask = mask0+mask1
        mask=mask4+mask3+mask2+mask1+mask0

    # set my output img to zero everywhere except my mask
        output_img = board.copy()
        output_img[np.where(mask==0)] = 0

    # or your HSV image, which I *believe* is what you want
        output_hsv = img_hsv.copy()
        output_hsv[np.where(mask==0)] = 0
        bgr_out=cv2.cvtColor(output_hsv,cv2.COLOR_HSV2BGR)

    #
        x,y,z=board.shape
        for i in range(3):
                for j in range(3):
                        img1=mask[(((i*x)/3)+8):((((i+1)*x)/3)-8),(((j*y)/3)+8):((((j+1)*y)/3)-8)]
            #gray=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)

            #ret,thresh1 = cv2.threshold(img1,10,255)
            #thresh = cv2.resize(thresh,(x, y)
            #kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(1,1))
            #res = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel)
                        contours,h = cv2.findContours(img1,1,2)

                        for cnt in contours:
                                approx = cv2.approxPolyDP(cnt,0.02*cv2.arcLength(cnt,True),True)
                                if len(approx)==3:
                                        board_shape[position]="Triangle"
                                        #cv2.drawContours(img1,[cnt],0,(0,255,0),-1)
                                elif len(approx)==4:
                                        board_shape[position]="4-sided"
                                        #cv2.drawContours(img1,[cnt],0,(0,0,255),-1)

                                elif len(approx) > 7:
                                        board_shape[position]="Circle"
                                        break
                                else :
                                        board_shape[position]="none"
                        position=position+1


        #print board_shape

        position=0
    
        ##board objects
        (x,y,z)=board.shape
        for i in range(3):
                for j in range(3):
                        position=position+1
                        img1=board[(((i*x)/3)):((((i+1)*x)/3)),(((j*y)/3)):((((j+1)*y)/3)),:]
                        gray=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
                        ret,thresh = cv2.threshold(gray,127,255,1)
                        contours,h = cv2.findContours(thresh,1,2)
                        cnt=contours[0]
                        (p,q,s)=img1.shape
                        (B,G,R)=img1[p/2,q/2]
                        if (B<10 and G<10 and R>200):
                                colour="red"
                        if (B<10 and R<10 and G>200):
                                colour="green"
                        if (G<10 and R<10 and B>200):
                                colour="blue"
                        if (B<10 and R>200 and G>200):
                                colour="yellow"

                        board_objects=  board_objects + [(position,colour,board_shape[(position-1)])]
                        board_area = board_area + [(cv2.contourArea(cnt),cv2.arcLength(cnt,True),colour)]
        position=0
        #print board_objects


        ##container objects
        (x,y,z)=container.shape
        for i in range(4):
                for j in range(4):
                        position=position+1
                        img1=container[(((i*x)/4)):((((i+1)*x)/4)),(((j*y)/4)):((((j+1)*y)/4)),:]
                        gray=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
                        ret,thresh = cv2.threshold(gray,127,255,1)
                        contours,h = cv2.findContours(thresh,1,2)
                        cnt=contours[0]
                        (p,q,s)=img1.shape
                        (B,G,R)=img1[p/2,q/2]
                        if (B<10 and G<10 and R>200):
                                colour='red'
                        if (B<10 and R<10 and G>200):
                                colour="green"
                        if (G<10 and R<10 and B>200):
                                colour="blue"
                        if (B<10 and R>200 and G>200):
                                colour="yellow"
                        if (B<10 and R<10 and G<10):
                                colour="none"

                        container_objects=  container_objects + [(position,colour,shape)]
                        container_area = container_area + [(cv2.contourArea(cnt),cv2.arcLength(cnt,True),colour)]

        #print container_objects
        #print container_area
        #print board_area
        position=0

        #matching
        flag=0
        for i in range(9):
                for j in range(16):
                        if board_objects[i][1]==container_objects[j][1] and board_area[i]==container_area[j] :
                                flag=1
                                output_list =output_list + [(i+1,j+1)]
                                break
                if flag==0:
                        output_list =output_list + [(i+1,0)]
                else:
                        flag=0

        #print output_list

	# #### NO EDIT AFTER THIS

# DO NOT EDIT
# return Expected output, which is a list of tuples. See Task1_Description for detail.
	return board_objects, output_list	



'''
Below part of program will run when ever this file (task1_main.py) is run directly from terminal/Idle prompt.

'''
if __name__ == '__main__':
    

	board_filepath = "test_images/board_8.jpg"    			# change filename of board provided to you 
	container_filepath = "test_images/container_3.jpg"		# change filename of container as required for testing

	main(board_filepath,container_filepath)

	cv2.waitKey(0)
	cv2.destroyAllWindows()    
