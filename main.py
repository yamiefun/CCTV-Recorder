import cv2
import json
import argparse
import multiprocessing as mp
from multiprocessing import Process, Queue, Pool
from utils.param import *
import os
def video_reader(arg):
    vid = arg[0]
    print("reader: ", vid)
    queue = arg[1]
    ipcam = cv2.VideoCapture(WEBCAMS[vid]['url'])
    FPS = ipcam.get(cv2.CAP_PROP_FPS)
    print("CCTV ", vid, " FPS: ", FPS)
    video_writer = cv2.VideoWriter("output/"+WEBCAMS[vid]['id']+".avi", cv2.VideoWriter_fourcc(*'XVID'), FPS, (1920, 1080))


    if not ipcam.isOpened():
        print("reader ", vid, " fail, ip: ", WEBCAMS[vid]['url'])
    while True:
        ret, frame = ipcam.read()
        if ret:
            video_writer.write(frame)

def create_output_dir():
    try :
        os.makedirs("./output")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    m = mp.Manager()  
    queue = m.Queue(maxsize=15)
    input_list = []
    num = len(WEBCAMS)

    create_output_dir()

    for i in range(num):
        input_list.append([i, queue])
    p = Pool(num)
    res = p.map(video_reader, input_list)
    p.close()
    p.join()
