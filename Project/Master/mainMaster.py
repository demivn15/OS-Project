import socket
import sys
from startConnectionMaster import startMaster

def main():
    print("--- Starting Master Orchestrator ---")
    nodeRegistry = startMaster()
    print("--- Starting Image Distribution ---")
    startDistribution(nodeRegistry, "test_image.jpg")

if __name__ == "__main__":
    main()
