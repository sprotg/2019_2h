import socket
import time

def perform_task(cmd):
    TCP_PORT = 29999
    BUFFER_SIZE = 1024
    TCP_IP = '10.130.58.11' #INDTAST DEN RIGTIGE IP-ADRESSE HER!
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(10)
    try:
        s.connect((TCP_IP, TCP_PORT))
        response = s.recv(BUFFER_SIZE)
    except socket.error:
        print("Socket error")
        s.close()

    st = "load /programs/{}.urp\n".format(cmd)
    s.send(bytearray(st,'utf8'))
    response = s.recv(BUFFER_SIZE)
    print(response)
    s.send(b"play\n")
    response = s.recv(BUFFER_SIZE)
    s.close()

def get_status():
    #programState
    TCP_PORT = 29999
    BUFFER_SIZE = 1024
    TCP_IP = '10.130.58.11' #INDTAST DEN RIGTIGE IP-ADRESSE HER!
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(10)
    try:
        s.connect((TCP_IP, TCP_PORT))
        response = s.recv(BUFFER_SIZE)
    except socket.error:
        print("Socket error")
        s.close()

    st = "programState\n"
    s.send(bytearray(st,'utf8'))
    response = s.recv(BUFFER_SIZE)
    s.close()
    if response.startswith(b'PLAYING'):
        return True
    else:
        return False

def program_state():
        TCP_PORT = 29999
        BUFFER_SIZE = 1024
        TCP_IP = '10.130.58.13'
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.settimeout(10)
        try:
            s.connect((TCP_IP, TCP_PORT))
            response = s.recv(BUFFER_SIZE)
        except socket.error:
            print("Fejl ved forbindelse")
            s.close()

        s.send(b"running\n")
        response = s.recv(BUFFER_SIZE)
        s.close()
        print(response)
        return response


def stop_robot():
    TCP_PORT = 29999
    BUFFER_SIZE = 1024
    TCP_IP = '10.130.58.11' #INDTAST DEN RIGTIGE IP-ADRESSE HER!
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(10)
    try:
        s.connect((TCP_IP, TCP_PORT))
        response = s.recv(BUFFER_SIZE)
    except socket.error:
        print("Socket error")
        s.close()

    s.send(b"stop\n")
    response = s.recv(BUFFER_SIZE)
    s.close()

cmd = ""

tilstand = 0

while cmd != 'q':

    if tilstand ==0:
        r = program_state()
        tilstand = 1
    if tilstand == 1:
        perform_task("fri")
        started=False
        tilstand = 2
    if tilstand == 2:
        time.sleep(1)

        r = program_state()
        if r.startswith(b'Program running: true'):
            print("Programmet er igang")
            started= True
        if r.startswith(b'Program running: false') and started==True:
            print("Programmet er afsluttet")
            tilstand = 3
    if tilstand == 3:
        cmd = input("Vælg kommando:")
    #if cmd == "play":


        #outputlogik
    if tilstand == 1:
        print("Robotten kører fri")
    if tilstand == 2:
        print("Venter....")
