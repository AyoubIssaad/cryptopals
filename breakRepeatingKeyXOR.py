import base64


# Reading the file content
text = open('6.txt', 'r')
textContent = text.read()
textContent = base64.b64decode(textContent)
# print(textContent)

# Let KEYSIZE to be guesses length of the key; try values from 2 to (say) 40.

keysize = 2

s1 = 'this is a test'
s2 = 'wokka wokka!!!'
s3 = 'geeksforgeeks'
s4 = 'geeksandgeeks'

assert len(s1) == len(s2)


def tobits(s):
    result = []
    for c in s:  # Loop through the characters of string
        bits = bin(ord(c))[2:]  # Convert character c to integer representing
        # the unicode character then to binary and remove first 2 characters 0b
        bits = '00000000'[len(bits):] + bits  # if length of bits is less than
        # 8 add 0 before
        result.extend([int(b) for b in bits])  # Extend to result a list of
        # integers
    return result


def hammingDistance(str1, str2):
    if len(str1) != len(str2):
        return False
    else:
        distance = 0
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                distance += 1
        return distance


print('Hamming distance = ', str(hammingDistance(tobits(s1), tobits(s2))))
# print(tobits(extContent))
textContentInBits = tobits(textContent)
print(textContentInBits[0:20])


for i in range(1, 41):
    # print(textContentInBits[0:i * 8])
    # print(textContentInBits[i * 8: (i+i) * 8])
    print(str(hammingDistance(textContentInBits[0:i * 8], textContentInBits[i * 8: (i+i) * 8])))
