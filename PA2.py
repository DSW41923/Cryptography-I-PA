import copy

from Crypto.Cipher import AES
from PA import split_by_length, strxor

# Phase 1: for PA only


def CBCDecryptor(key, ciphertext):
    byte_key = key.decode('hex')
    cipher = AES.new(key=byte_key)

    byte_ct = ciphertext.decode('hex')
    split_ct = split_by_length(byte_ct, 16)
    iv = split_ct[0]

    result = []

    for index, block_ct in enumerate(split_ct[1:]):
        if index == 0:
            block_pt = strxor(cipher.decrypt(block_ct), iv)
        else:
            block_pt = strxor(cipher.decrypt(block_ct), split_ct[index])
        result.append(block_pt)

    return ''.join(result)


def CTRDecryptor(key, ciphertext):
    byte_key = key.decode('hex')
    cipher = AES.new(key=byte_key)

    byte_ct = ciphertext.decode('hex')
    split_ct = split_by_length(byte_ct, 16)
    iv = split_ct[0]

    result = []

    for index, block_ct in enumerate(split_ct[1:]):
        block_iv = copy.deepcopy(iv)
        split_block_iv = split_by_length(block_iv, 1)
        split_block_iv[-1] = chr(ord(split_block_iv[-1]) + index)
        block_iv = ''.join(split_block_iv)
        block_pt = strxor(cipher.encrypt(block_iv), block_ct)
        result.append(block_pt)

    return ''.join(result)


q1 = CBCDecryptor('140b41b22a29beb4061bda66b6747e14',
                  '4ca00ff4c898d61e1edbf1800618fb2828a226d160dad0' +
                  '7883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81')
q2 = CBCDecryptor('140b41b22a29beb4061bda66b6747e14',
                  '5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab' +
                  '7da33249de7d4afc48e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253')
q3 = CTRDecryptor('36f18357be4dbd77f050515c73fcf9f2',
                  '69dda8455c7dd4254bf353b773304eec0ec7702330098c' +
                  'e7f7520d1cbbb20fc388d1b0adb5054dbd7370849dbf0b' +
                  '88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329')
q4 = CTRDecryptor('36f18357be4dbd77f050515c73fcf9f2',
                  '770b80259ec33beb2561358a9f2dc617e46218c0a53cbe' +
                  'ca695ae45faa8952aa0e311bde9d4e01726d3184c34451')

print q1
print q2
print q3
print q4
