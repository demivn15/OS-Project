import socket
from handShakeMaster import performMasterHandshake

masterIP = "172.20.8.3"
port = 5000

def startMaster(): 
    connectedNodes = {}
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((masterIP, port))
        s.listen(3)
        print(f"[@] Master (PC) listening on {masterIP}:{port}")
        while len(connectedNodes) < 3:
            conn, addr = s.accept()
            identity = conn.recv(1024).decode()
            print(f"[+] Connection attempt from: {addr[0]}")
            conn.sendall(b"ACK_master")
            nodeRole = performMasterHandshake(conn, addr)
            connectedNodes[addr[0]] = {"role": nodeRole, "socket": conn}
    print(f"[+] Node {nodeRole} registered at {addr[0]}")
    return connectedNodes
