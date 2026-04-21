import socket
from handShakeWorker import sendWorkerHandshake

masterIP = "172.20.8.3"
port = 5000

def startNode(nodeRole, role):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((masterIP, port))
        s.sendall(nodeRole.encode())
        sendWorkerHandshake(s)
        return s
    except Exception as e:
        print(f"[!] Error: {e}")
        return None
