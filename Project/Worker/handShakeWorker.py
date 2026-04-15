import socket
import pickle
import os

def sendWorkerHandshake(s):
    handshakePacket = {
        "role": "worker", 
        "cores": os.cpu_count(),
        "msg": "Requesting instructions"
    }
    s.sendall(pickle.dumps(handshakePacket))
    rawResponse = s.recv(4096)
    response = pickle.loads(rawResponse)
    if response.get("status") == "READY":
        print("[+] Handshake complete. Master has promoted us to ACTIVE state.")
