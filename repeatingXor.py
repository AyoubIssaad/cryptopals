stanza = b"Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
key = b"ICE"


def repeating_char_xor(input_bytes, key_values):
    """ Returns the result of each byte being XOR'd with a repeating sequence
    of chars from key_values"""
    output_bytes = b''
    index = 0
    for byte in input_bytes:
        output_bytes += bytes([byte ^ key_values[index]])
        if index == (len(key_values) - 1):
            index = 0
        else:
            index += 1
    return output_bytes


xords = repeating_char_xor(stanza, key)
print(xords.hex())
