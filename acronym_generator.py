user_input = input('Enter a phrase or press "q" to exit: ')

#phrase = (user_input.replace('of','')).split()
phrase = user_input.split()
_phrase = ''

for word in phrase:
    if user_input.lower() == 'q':
        break
    if word.lower() == 'of':
            continue
    for s in word:
        if s == word[0]:
           _phrase += word[0].upper()
        else:
            break 
print(_phrase)
