from enum import IntEnum
import struct
from typing import List, Optional, Tuple

class VariantType(IntEnum):
    UNKNOWN = 0
    FLOAT = 1
    STRING = 2
    VEC2 = 3
    VEC3 = 4
    UNSIGNED = 5
    SIGNED = 9

class Variant:
    def __init__(self, value, variant_type: VariantType):
        self.value = value
        self.variant_type = variant_type

    def as_string(self) -> str:
        if self.variant_type == VariantType.FLOAT:
            return str(self.value)
        elif self.variant_type == VariantType.STRING:
            return self.value
        elif self.variant_type == VariantType.VEC2:
            return f"({self.value[0]}, {self.value[1]})"
        elif self.variant_type == VariantType.VEC3:
            return f"({self.value[0]}, {self.value[1]}, {self.value[2]})"
        elif self.variant_type == VariantType.UNSIGNED:
            return str(self.value)
        elif self.variant_type == VariantType.SIGNED:
            return str(self.value)
        else:
            return "Unknown"

    def as_int32(self) -> int:
        if self.variant_type == VariantType.SIGNED:
            return self.value
        return 0
    
    def as_vec2(self) -> Tuple[float, float]:
        if self.variant_type == VariantType.VEC2:
            return self.value
        return (0.0, 0.0)
    
    def as_uint32(self) -> int:
        if self.variant_type == VariantType.UNSIGNED:
            return self.value
        return 0
    
    def as_float(self) -> float:
        if self.variant_type == VariantType.FLOAT:
            return self.value
        return 0.0
    
    def as_vec3(self) -> Tuple[float, float, float]:
        if self.variant_type == VariantType.VEC3:
            return self.value
        return (0.0, 0.0, 0.0)
    
    def __repr__(self):
        return f"Variant({self.variant_type.name}: value={self.value})"

class VariantList:
    def __init__(self):
        self.variants: List[Variant] = []

    @classmethod
    def deserialize(cls, data: bytes) -> 'VariantList':
        if len(data) == 0:
            raise ValueError("Data is empty, cannot deserialize VariantList.")
        
        variant_list = cls()
        offset = 0

        size = data[offset]
        offset += 1

        for _ in range(size):
            if offset >= len(data):
                raise ValueError("Unexpected end of data while deserializing VariantList.")
            
            _index = data[offset]
            offset += 1

            if offset >= len(data):
                raise ValueError("Unexpected end of data while deserializing VariantList.")
            vtype = data[offset]
            offset += 1

            if vtype == VariantType.FLOAT:
                if offset + 4 > len(data):
                    raise ValueError("Not enough data for FLOAT variant.")
                value = struct.unpack('<f', data[offset:offset+4])[0]
                offset += 4
                variant = Variant(value, vtype)

            elif vtype == VariantType.STRING:
                if offset + 4 > len(data):
                    raise ValueError("Not enough data for STRING length.")
                str_len = struct.unpack('<I', data[offset:offset+4])[0]
                offset += 4

                if offset + str_len > len(data):
                    raise ValueError("Not enough data for STRING content.")
                value = data[offset:offset+str_len].decode('utf-8')
                offset += str_len
                variant = Variant(value, vtype)

            elif vtype == VariantType.VEC2:
                if offset + 8 > len(data):
                    raise ValueError("Not enough data for VEC2 variant.")
                x, y = struct.unpack('<ff', data[offset:offset+8])
                offset += 8
                variant = Variant((x, y), vtype)

            elif vtype == VariantType.VEC3:
                if offset + 12 > len(data):
                    raise ValueError("Not enough data for VEC3 variant.")
                x, y, z = struct.unpack('<fff', data[offset:offset+12])
                offset += 12
                variant = Variant((x, y, z), vtype)

            elif vtype == VariantType.UNSIGNED:
                if offset + 4 > len(data):
                    raise ValueError("Not enough data for UNSIGNED variant.")
                value = struct.unpack('<I', data[offset:offset+4])[0]
                offset += 4
                variant = Variant(value, vtype)

            elif vtype == VariantType.SIGNED:
                if offset + 4 > len(data):
                    raise ValueError("Not enough data for SIGNED variant.")
                value = struct.unpack('<i', data[offset:offset+4])[0]
                offset += 4
                variant = Variant(value, vtype)

            else:
                variant = Variant(None, vtype)

            variant_list.variants.append(variant)

        return variant_list

    def get(self, index: int) -> Optional[Variant]:
        if 0 <= index < len(self.variants):
            return self.variants[index]
        return None

    def __len__(self):
        return len(self.variants)

    def __getitem__(self, index):
        return self.variants[index]

    def __iter__(self):
        return iter(self.variants)

    def __repr__(self):
        return f"VariantList({self.variants})"