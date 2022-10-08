import cv2 as cv

#read video
capture = cv.VideoCapture("videos\dog.mp4")

#resize function
def resize_scale (frame , scale) :
    width  = int( frame.shape[1] * scale) 
    height = int( frame.shape[0] * scale) 
    dim = (width , height)
    return cv.resize ( frame , dim , interpolation = cv.INTER_AREA)


#change res
def change_res (width , height) :
    capture.set( 3 , width)
    capture.set( 4 , height)
         

#show video [reading frame by frame]
while True :
    #here read frame by frame
    isTrue , frame = capture.read()
    #show video normal
    cv.imshow( "cat" , frame )
    

    '''
     #here read frame by frame
    frame_resized = resize_scale (frame , 0.75)    
    
    '''
    #here read frame by frame

    change_res (100 , 50 )
    #show video_resized
    cv.imshow( "cat_resized_res" , frame )


    #breaking video
    if cv.waitKey(1) & 0xFF == ord ('q') :
        break

capture.release ()
cv.destroyAllWindows()

