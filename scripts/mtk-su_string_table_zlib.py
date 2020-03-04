# written by the pontiacbandit
import zlib
import struct

ZLIB_OFFESET = 0xF098
ZLIB_COMPRESSED_SIZE = 0x4EC
ZLIB_DECOMPRESSED_SIZE = 0xDA1
SECRET = 0x25A104A8

def decompress_payload():
    f = open("mtk-su", "rb")
    f.seek(ZLIB_OFFESET)
    compression = list(f.read(ZLIB_COMPRESSED_SIZE))

    secret = struct.pack("<I", SECRET)

    for i, b in enumerate(secret):
        compression[i] = compression[i] ^ b

    dec = zlib.decompress(bytes(compression))
    assert len(dec) == ZLIB_DECOMPRESSED_SIZE

    return dec


def get_relevant_strings(s):
    strlen = lambda s: s.find(b'\x00')

    ret = ["", "", ""]
    offset = 0
    while (True):
        length = strlen(s[offset:])
        string = s[offset:offset + length].decode("utf-8")
        if length == -1:
            break

        sig = 0
        for i in range(length):
            sig = (sig * 31 + s[offset + i]) % 0x100000000

        if sig == 0x6D7A00FC:
            ret[0] = string
        elif sig == 0x4B4AB49B:
            ret[1] = string
        elif sig == 0x6F35A3FF:
            ret[2] = string

        offset += length + 1

    return ret

strings = decompress_payload()
rel_strings = get_relevant_strings(strings)
print(rel_strings)
