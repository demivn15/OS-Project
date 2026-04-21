import socket
import sys
from startConnectionWorker import startNode
from protocol import receivePacket
from runWorker import runWorker

def main():
    if len(sys.argv) < 2:
        role = "worker"
    else:
        role = sys.argv[1]
    print(f"--- Starting {role} Node ---")
    sock = startNode(role, role) 
    if sock:
        runWorker(sock)

if __name__ == "__main__":
    main()
