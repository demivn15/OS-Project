import socket
import pickle

def performMasterHandshake(conn, addr):
    rawData = conn.recv(4096)
    handshakeData = pickle.loads(rawData)
    nodeRole = handshakeData.get("role")
    nodeCores = handshakeData.get("cores")
    print(f"[*] Handshake received from {nodeRole} at {addr}")
    print(f"[*] System Info: {nodeCores} cores detected.")
    ack_packet = {"status": "READY", "session_id": 101}
    conn.sendall(pickle.dumps(ack_packet))
    return nodeRole
