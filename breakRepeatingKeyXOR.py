import base64


# Reading the file content
text = open('6.txt', 'r')
textContent = text.read()
textContent = base64.b64decode(textContent)
# print(textContent)

# Let KEYSIZE to be guesses length of the key; try values from 2 to (say) 40.

# keysize = 2

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
ciphertext = tobits(textContent)
print(ciphertext[0:20])

# Take the keysize from suggested range
for keysize in range(2, 41):

    # Initialize list to store Hamming distances for this keysize
    distance = []

    # Break the ciphertext into chunks the length of the keysize
    chunks = [ciphertext[i:i+keysize] for i in range(0, len(ciphertext), keysize)]
    while True:
        try:
            # Take the two chunks at the beginning of the list and get the
            # hamming distance
            chunk_1 = chunks[0]
            chunk_2 = chunks[1]
            distance = hammingDistance(chunk_1, chunk_2)

            # Nrmalize this resukt by dividing by KEYSIZE
            distance.append(distance/keysize)

            # Remove these chunks so when the loop starts over, the hamming
            # distance for the next two chunks can be calculated
            del chunks[0]
            del chunks[1]

        # WHen an exception occurs (indicating all chunks have been processed)
        # break out of the loop.
        except Exception as e:
            break
