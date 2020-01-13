import singleByteXor


text = open('4.txt', 'r')
textContent = text.read()
tableOfHexs = textContent.split('\n')

potential_messages = []

for line in tableOfHexs:
    ciphertex = bytes.fromhex(line)
    for key_value in range(256):
        message = singleByteXor.single_char_xor(ciphertex, key_value)
        score = singleByteXor.get_english_score(message)
        data = {
            'message': message,
            'score': score,
            'key': key_value,
            'original_hex': line}
        potential_messages.append(data)


best_score = sorted(potential_messages, key=lambda x: x['score'],
                    reverse=True)[0]

for item in best_score:
    print("{}: {}".format(item.title(), best_score[item]))
