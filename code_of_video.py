import cv2
import image_dehazer

video_path='WhatsApp Video 2024-02-10 at 2.31.03 PM.mp4'
cap=cv2.VideoCapture(video_path)

fps=cap.get(cv2.CAP_PROP_FPS) #taking the frames of a video clip as a property
width=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
total_frames=int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

#create video_writer object to write dehazed frame
output_path='output_video_dehazed.avi'
fourcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter(output_path,fourcc,fps,(width,height))

#loop through the frames
while True:
    ret,frame=cap.read()
    if not ret:
        break;
    #remove haze
    Haze_corrected_img,haze_map=image_dehazer.remove_haze(frame)

    #write the dehazed frame to output video
    out.write(Haze_corrected_img)

    #display the original hazy frame and dehazed frane

    cv2.imshow('input frame',frame)
    cv2.imshow('enhanced_frame',Haze_corrected_img)

    #break the loop if z is pressed
    if cv2.waitKey(10) & 0xFF==ord('z'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()



