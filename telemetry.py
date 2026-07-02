import socket

HOST = "0.0.0.0"
PORT = 20777

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))

print("Listening for telemetry...")


def receive_packet():
    data, address = sock.recvfrom(4096)
    return data