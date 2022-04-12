alphabets = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]

def ceaser_cipher(text, shift_value):
    """Returns a ceaser-ciphered string."""
    encrypted_text = ''
    
    for i in text:
        # char = text[i]
        for alphabet in alphabets:
            if i.isupper():
                encrypted_text += (alphabets[(alphabets.index(i) + shift_value) % 26]).upper()
                break    
            elif i.islower():
                encrypted_text += (alphabets[(alphabets.index(i.upper()) + shift_value) % 26]).lower()
                break
                
    return encrypted_text


def decipher_ceaser(crypted_text,shift_value):

    decrypted_text = ""
    for i in crypted_text:
        for alphabet in alphabets:
            if i.isupper():
                decrypted_text += (alphabets[(alphabets.index(i) - shift_value) % 26]).upper()
                break    
            elif i.islower():
                decrypted_text += (alphabets[(alphabets.index(i.upper()) - shift_value) % 26]).lower()
                break
    return decrypted_text


def decipher_or_cipher(text,shift_value,choice='decipher'):
    """Ciphers or deciphers text depending on your choice"""
    if choice.lower() == 'decipher':
        return decipher_ceaser(text,shift_value)
    elif choice.lower() == 'cipher':
        return ceaser_cipher(text,shift_value)





print(f"The ciphered text is {ceaser_cipher('Python',5)}")
print(f"The deciphered text is {decipher_ceaser(ceaser_cipher('Python',5), 5)}")
#Type in cipher to cipher or decipher to dicipher text."
print(decipher_or_cipher('Udymts',5, 'decipher'))


