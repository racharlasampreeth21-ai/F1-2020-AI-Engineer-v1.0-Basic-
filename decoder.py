import struct
from parser import get_packet_id

HEADER_SIZE = 24
CAR_TELEMETRY_SIZE = 58


def get_player_index(packet):
    return struct.unpack_from("<B", packet, 22)[0]


def decode(packet):

    packet_id = get_packet_id(packet)

    if packet_id == 6:
        return decode_car_telemetry(packet)

    return None


def decode_car_telemetry(packet):

    player_index = get_player_index(packet)

    start = HEADER_SIZE + (player_index * CAR_TELEMETRY_SIZE)

    return {

        "packet": "Car Telemetry",

        "speed": struct.unpack_from("<H", packet, start)[0],

        "throttle": struct.unpack_from("<f", packet, start + 2)[0],

        "steer": struct.unpack_from("<f", packet, start + 6)[0],

        "brake": struct.unpack_from("<f", packet, start + 10)[0],

        "clutch": struct.unpack_from("<B", packet, start + 14)[0],

        "gear": struct.unpack_from("<b", packet, start + 15)[0],

        "rpm": struct.unpack_from("<H", packet, start + 16)[0],

        "drs": struct.unpack_from("<B", packet, start + 18)[0],

        "rev_lights": struct.unpack_from("<B", packet, start + 19)[0],
    }