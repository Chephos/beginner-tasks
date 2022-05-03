import string,re


str1 = "Hello. I'm Edwin A.J, and you?"
str2 = "What time is it? Hammer time."
def reverse_order(phrase):
    """Returns the reverse of the input but maintains the position of the punctuations"""
    splt=re.findall(r"[\w'.-]+[\w]|[\s]|[.,!?:;]", phrase)
    temporaryList = []
    tempWord = []
    word = ''
    for char in splt:
        if char not in string.punctuation:
            word = char + word
        else:
            word = word.rstrip()
            
            tempWord.append(word)
            tempWord.append(char)
            word = ''

    punctuations = {}
    
    for index,char in enumerate(tempWord):
        if char not in string.punctuation:
            temporaryList.insert(0,char)
        else:
            punctuations[index] = char
           
    
    for k,v in punctuations.items():
        temporaryList.insert(k,f"{v} ")


    word = ''.join(temporaryList)
    word = word[0].upper() + word[1:]
    print(word)
    return word
  

reverse_order(str2)