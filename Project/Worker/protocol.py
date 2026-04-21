import pickle
import struct

def preparePacket(dataObject):
    payload = pickle.dumps(dataObject)
    header = struct.pack('I', len(payload))
    return header + payload

def receivePacket(sock):
    header = sock.recv(4)
    if not header:
        return None
    payloadSize = struct.unpack('I', header)[0]
    data = b''
    while len(data) < payloadSize:
        packet = sock.recv(payloadSize - len(data))
        if not packet:
            break
        data += packet
    return pickle.loads(data)
