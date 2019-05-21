import time
import zmq

def producer():
    context = zmq.Context()
    zmq_socket = context.socket(zmq.PUSH)
    zmq_socket.bind("tcp://129.118.107.227:5558")
    # Start your result manager and workers before you start your producers
    
    num = 10
    work_message = { 'num' : num }
    zmq_socket.send_json(work_message)
    print("Sending {}".format(num))

producer()
