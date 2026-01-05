import ctypes
import hashlib

def sha256(data: str) -> str:
    data = str(data)
    return hashlib.sha256(data.encode('utf-8')).hexdigest()

def md5(data: str) -> str:
    data = str(data)
    return hashlib.md5(data.encode('utf-8')).hexdigest()

def string(data: str) -> int:
    if not data:
        return 0

    acc = ctypes.c_uint32(0x55555555)
    for char in data:
        acc.value = (acc.value >> 27) + (acc.value << 5) + ord(char)
    return acc.value