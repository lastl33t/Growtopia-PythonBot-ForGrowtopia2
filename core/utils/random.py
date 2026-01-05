import random

def hex(length: int, uppercase: bool = False) -> str:
    hex_chars = '0123456789abcdef'
    hex_string = ''.join(random.choice(hex_chars) for _ in range(length))
    return hex_string.upper() if uppercase else hex_string

def mac() -> str:
    mac_parts = [hex(2) for _ in range(6)]
    return ':'.join(mac_parts)