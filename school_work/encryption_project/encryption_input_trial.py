from pynput.mouse import Button, Controller
from time import *
from caesar_cipher import decrypt

mouse = Controller()

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def encrypt(plaintext, key):
    ciphertext = []
    pos = -1
    for i in plaintext:
        pos += 1
        if i in alphabet:
            alphabet_index = alphabet.index(i)
            new_key = alphabet_index + key[pos]
            if new_key >= 26:
                new_key = (alphabet_index + key[pos]) - 26
            ciphertext.append(alphabet[new_key])
        else:
            ciphertext.append(i) # for special characters
    ciphertext = ("".join(ciphertext))
    return ciphertext, key[:len(ciphertext)]

def make_key(message):
    key_list = []
    new_key_list = []
    for i in range(0, 5):
        key_list.append(mouse.position)
        sleep(0.4)

    for i in key_list:
        i = list(i)
        if 0.0 in i: #don't want characters to stay same
            i.remove(0.0)
        for x in i:
            # here is where they should be converted to double digits
            new_key_list.append(round(x/100))

    while len(new_key_list) < len(message):
        new_key_list = 2*new_key_list #repeat key if not as long as the message 

    return new_key_list

message = "abcdefghijklmopqrstuvwxyzabc"
key = make_key(message)
print(encrypt(message.upper(), key))
