import socket
from handShakeWorker import sendWorkerHandshake

masterIP = "172.20.8.3"
port = 5000

def startNode(nodeRole, role):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            print(f"[@] {nodeRole} attempting to connect to Master at {masterIP}...")
            s.connect((masterIP, port))
            s.sendall(nodeRole.encode())
            response = s.recv(1024).decode()
            if response == "ACK_master":
                print(f"[+] Connection Verified. {nodeRole} is online.")
                sendWorkerHandshake(s, role)
                
    except ConnectionRefusedError:
        print("[!] Error: Master is not online or IP is incorrect.")
    except Exception as e:
        print(f"[!] Unexpected Error: {e}")
