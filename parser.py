import struct

PACKET_TYPES = {
    0: "Motion",
    1: "Session",
    2: "Lap Data",
    3: "Event",
    4: "Participants",
    5: "Car Setups",
    6: "Car Telemetry",
    7: "Car Status"
}


def get_packet_id(packet):
    return struct.unpack_from("<B", packet, 5)[0]


def get_packet_name(packet_id):
    return PACKET_TYPES.get(packet_id, "Unknown Packet")