import socket
from handShakeMaster import performMasterHandshake

masterIP = "172.20.8.3"
port = 5000

def startMaster(): 
    connectedNodes = {}
    # Use REUSEADDR to allow quick restarts on your Mint/Debian system
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((masterIP, port))
        s.listen(3)
        print(f"[@] Master (PC) listening on {masterIP}:{port}")
        
        while len(connectedNodes) < 3:
            conn, addr = s.accept()
            with conn:
                # 1. Initial Connection Identification
                identity = conn.recv(1024).decode()
                print(f"[+] Connection attempt from: {addr[0]}")
                conn.sendall(b"ACK_master")
                
                # 2. Formal Protocol Handshake (Pickle-based)
                # This uses the connection to get cores and role
                nodeRole = performMasterHandshake(conn, addr)
                connectedNodes[addr[0]] = nodeRole

    print("\n[!] Phase 1 Complete. Network Topology Verified.")
    print(f"Active Cluster Nodes: {connectedNodes}")
