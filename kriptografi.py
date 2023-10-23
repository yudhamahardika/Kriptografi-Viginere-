def generateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return key
    else:
        for i in range(len(string) - len(key)):
            key.append(key[i % len(key)])
    return ''.join(key)

def cipherText(string, key):
    cipher_text = []
    for i in range(len(string)):
        x = (ord(string[i]) + ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    return ''.join(cipher_text)

def originalText(cipher_text, key):
    orig_text = []
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) - ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    return ''.join(orig_text)

# Driver code
if __name__ == "__main__":
    input_text = "YUDHAMAHARDI"
    keyword = "AYUSH"
    key = generateKey(input_text, keyword)
    encrypted_text = cipherText(input_text, key)
    decrypted_text = originalText(encrypted_text, key)

    print("Input Teks       : " + input_text)
    print("Kunci Enkripsi   : " + key)
    print("Enkripsi Teks    : " + encrypted_text)
    print("Dekripsi Teks    : " + decrypted_text)
