def ceaser_cipher(text, shift_value):
    """Returns a ceaser-ciphered string."""
    alphabets = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    encrypted_text = ''
    
    #Traverse the text and loop through the list
    for i in text:
        for alphabet in alphabets:
            #check if the string is upper or lower case
            if i.isupper():
                # get the index of the string within the list
                # add the shift value to it
                # find the modulos of their sum 
                # index the alphabets list using the modulos as index
                # append to the string
                encrypted_text += (alphabets[(alphabets.index(i) + shift_value) % 26]).upper()
                break    
            elif i.islower():
                encrypted_text += (alphabets[(alphabets.index(i.upper()) + shift_value) % 26]).lower()
                break
                
    return encrypted_text


def decipher_ceaser(crypted_text,shift_value):
    """Deciphers the given text."""

    alphabets = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]

    decrypted_text = ""
    #Traverse the text and loop through the list
    for i in crypted_text:
        for alphabet in alphabets:
            #check if the string is upper or lower case
            if i.isupper():
                # get the index of the string within the list
                # subtract the shift value from it
                # find the modulos of their difference
                # index the alphabets list using the modulos as index
                # append to the string
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
