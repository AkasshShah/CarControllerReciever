import os
import socket
import struct
import sys
import netifaces
import time
import json
import threading
import multiprocessing 
import ServerSocket as SS
import HandleGPIO as GP
import videoFeed as VF

def handle_json(filename):
    global config
    f = open(filename)
    config = json.load(f)
    f.close()
    SS.ServerIP = SS.getIP(interface=config["LAN_Interface"])
    SS.CameraPort = config["CameraPort"]
    SS.ServerPort = config["ControllerPort"]


if __name__ == "__main__":
    handle_json('config.json')
    print(sys.argv)
    # with open("pids.txt", "w") as file1:
    #     L = ["bash pid: " + str(sys.argv[-1]), "\npyth pid: " + str(os.getpid())]
    #     file1.writelines(L)
    print("starting at", SS.ServerIP, "on port", SS.ServerPort, "pid: ", os.getpid())
    connection = None
    sock = SS.startSocket()
    sock.listen(1)
    sockState = SS.possibleStates[0]
    frState = {"r": 0.0, "f": 0.0}
    try:
        car = GP.Car(config["GPIO_pinAssignment"]["BackMotor1"], config["GPIO_pinAssignment"]["BackMotor2"], config["GPIO_pinAssignment"]["FrontServoSignalPin"], config["GPIO_pinAssignment"]["FrontServoReverser"], config["GPIO_pinAssignment"]["ThrottleMaxAfter"])
        if config["CameraOn"]:
            camera = VF.startCam(height=config["CameraSetup"]["height"], width=config["CameraSetup"]["width"], frameRate=config["CameraSetup"]["framerate"], rotation=config["CameraSetup"]["rotation"])
            cameraServer = VF.StreamingServer((SS.ServerIP, SS.CameraPort), VF.StreamingHandler)
            # p = threading.Thread(target=cameraServer.serve_forever)
            p = multiprocessing.Process(target=cameraServer.serve_forever)
            p.start()
            # cameraServer.serve_forever()
        while True:
            if sockState == SS.possibleStates[0]:
                try:
                    print('waiting for a connection at', SS.ServerIP, SS.ServerPort)
                    connection, address = sock.accept()
                    print("connected from", address)
                    sockState = SS.possibleStates[1]
                except:
                    connection.close()
                    break
            if sockState == SS.possibleStates[1]:
                received_message = connection.recv(1024)
            if received_message:
                sockState = SS.possibleStates[1]
                frState = SS.handleMessage(received_message, frState, sockState, connection, sock)
                # set GPIO Pins according to frState
                car.setFR(f=frState["f"], r=frState["r"])
    finally:
        print("cleaning up")
        if config["CameraOn"]:
            VF.stopCam(camera)
            p.terminate()
            p.join()
            # exit()
