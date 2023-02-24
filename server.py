import zmq
import time


context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")


def get_alternative_equipment(equipment):
    
    alternative_equipment = {"treadmill": "stationary bikes", "Kettlebells": "Dumbbell", "Ellipticals": "Assault Bike"}
    return alternative_equipment.get(equipment, " ")


while True:
    
    equipment = socket.recv().decode()

    time.sleep(1)

    fitness_equipemt = get_alternative_equipment(equipment)

    socket.send(fitness_equipemt.encode())