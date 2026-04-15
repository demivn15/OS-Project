import socket
import sys
from startConnectionWorker import startNode

def main():
    if len(sys.argv) < 2:
        role = "worker"
    else:
        role = sys.argv[1]
    print(f"--- Starting {role} Node ---")
    startNode(role, role) 

if __name__ == "__main__":
    main()
