import ctypes

def read_u32(pointer):
    return ctypes.cast(pointer, ctypes.POINTER(ctypes.c_uint32)).contents.value