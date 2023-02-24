import zmq

context = zmq.Context()

print("Connecting to the Busy Gym server...")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")
print(f"Current libzmq version is {zmq.zmq_version()}")
print(f"Current  pyzmq version is {zmq.__version__}")
for request in range(1):
    print(f"Sending request {request} ...")
    socket.send_string("Kettlebells")

    message = socket.recv()
    print(f"Received reply {request} [ {message} ]")