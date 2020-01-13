def xor(str1, str2):
    # Check if same length
    if len(str1) != len(str2):
        return False
    # Convert to binaries
    uncoded1 = int(str1, 16)
    uncoded2 = int(str2, 16)
    return hex(uncoded1 ^ uncoded2)[2:]


a = "1c0111001f010100061a024b53535009181c"
b = "686974207468652062756c6c277320657965"
c = "746865206b696420646f6e277420706c6179"
assert xor(a, b) == c

# print(str(xor('1c0111001f010100061a024b53535009181c',
# '686974207468652062756c6c277320657965')))
# print(hex2base64.hexStringToBase64('1c0111001f010100061a024b53535009181c'))
