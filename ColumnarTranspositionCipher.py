def parse_key(key):
    key = key.upper()
    tmp = [(i, k) for i, k in enumerate(key)]
    tmp = sorted(tmp, key=lambda x: x[1])

    enc_table = {}
    dec_table = {}
    for i, r in enumerate(tmp):
        enc_table[r[0]] = i
        dec_table[i] = r[0]

    return enc_table, dec_table


def transposition_encrypt(text, key):
    msgsize = len(text)
    keysize = len(key)
    result = ""
    
    filler = ""
    if msgsize % keysize != 0:
        filler = "0" * (keysize - msgsize % keysize)

    text = text.upper() + filler
    enc_table, _ = parse_key(key)

    buf = [""] * keysize
    for i, c in enumerate(text):
        col = i % keysize
        index = enc_table[col]
        buf[index] += c

    for part in buf:
        result += part

    return result

def transposition_decrypt(ciphertext, key):
    msgsize = len(ciphertext)
    keysize = len(key)
    result = ""

    _, dec_table = parse_key(key)

    blocksize = int(msgsize / keysize)
    buf = [""] * keysize
    pos = 0
    for i in range(keysize):
        part = ciphertext[pos:pos + blocksize]
        index = dec_table[i]
        buf[index] += part
        pos += blocksize

    for i in range(blocksize):
        for j in range(keysize):
            if buf[j][i] != "0":
                result += buf[j][i]

    return result

plaintext = "ILOVEYOUSOMUCHREALLY"
key = "LIOV"

print(f"평문 : {plaintext.upper()}")

ciphertext = transposition_encrypt(plaintext, key)
print(f"암호화 : {ciphertext}")

decrypted_text = transposition_decrypt(ciphertext, key)
print(f"복호화 : {decrypted_text}")
