
# ! for decrypt : encrypt = -1
# ! for encrypt : encrypt = 1
# ! for text : text that is to be encrypted
def encrypt(text, encrypt=1):
    return_string = ""
    for i in text:
        return_string += chr(ord(i)+(3*encrypt))
    return return_string


encrypted_text = encrypt("Hey there!")
print(encrypted_text)
decrypted_text = encrypt(encrypted_text, encrypt=-1)
print(decrypted_text)
