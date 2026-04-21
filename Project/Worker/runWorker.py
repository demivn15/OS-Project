import socket
import sys
from startConnectionWorker import startNode
from protocol import receivePacket

def runWorker(sock):
    print("[@] Worker listening for image chunks...")
    try:
        while True:
            packet = receivePacket(sock)
            if packet:
                chunk_id = packet.get("chunkID")
                print(f"[+] Received chunk {chunk_id}")
            else:
                print("[!] Master disconnected.")
                break
    except KeyboardInterrupt:
            print(f"[!] : Worker shutting down...")
    finally:
        sock.close()
        print(f"[-] Socket closed.")
