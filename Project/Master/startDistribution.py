from imageProcessor import sliceImage
from protocol import preparePacket

def startDistribution(connectedNodes, imagePath):
    slices = sliceImage(imagePath)
    workerNodes = [node for node in connectedNodes.values() 
                   if "worker" in node["role"].lower()]
    if not workerNodes:
        print(f"[!] No workers available for distribution.")
        return
    for i, chunk in enumerate(slices):
        node = workerNodes[i % len(workerNodes)]
        sock = node["socket"]
        metadata = {"chunkID": i, "filter": "grayscale", "data": chunk}
        sock.sendall(preparePacket(metadata))
        print(f"[+] Dispatched chunk {i} to {node['role']}")
