from enum import IntFlag

class ItemFlag(IntFlag):
    FLIPPABLE       = 0x1
    EDITABLE        = 0x2
    SEEDLESS        = 0x4
    PERMANENT       = 0x8
    DROPLESS        = 0x10
    NO_SELF         = 0x20
    NO_SHADOW       = 0x40
    WORLD_LOCKED    = 0x80
    BETA            = 0x100
    AUTO_PICKUP     = 0x200
    MOD_FLAG        = 0x400
    RANDOM_GROW     = 0x800
    PUBLIC          = 0x1000
    FOREGROUND      = 0x2000
    HOLIDAY         = 0x4000
    UNTRADEABLE     = 0x8000

    @classmethod
    def from_bits(cls, bits: int) -> "ItemFlag":
        return cls(bits)