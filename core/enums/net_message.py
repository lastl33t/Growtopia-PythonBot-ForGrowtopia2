from enum import Enum

class NetMessage(Enum):
    Unknown = 0
    ServerHello = 1
    GenericText = 2
    GameMessage = 3
    GamePacket = 4
    Error = 5
    Track = 6
    ClientLogRequest = 7
    ClientLogResponse = 8
    Max = 9