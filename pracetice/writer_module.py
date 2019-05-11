import cv2


class mp4_writer:
    def __init__(self,out_path,frame_size):
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        self.out1 = cv2.VideoWriter(out_path,fourcc,10,frame_size,True)
    def write(self,frame):
        self.out1.write(frame)
    def release(self):
        self.out1.release()

