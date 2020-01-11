# This code converts hex to base64

import codecs  # Using codecs library to convert


def hexStringToBase64(hex):
    decodedHex = codecs.decode(hex, 'hex')  # Converts to hex bytes
    # Converts bytes to base64
    return codecs.encode(decodedHex, 'base64').decode()


# hex = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
# print(hexStringToBase64(hex))
# print(codecs.decode(hex, 'hex'))
# print('--------------------')
# print(bytes.fromhex(hex))
