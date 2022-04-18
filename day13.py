import string
sentence = input("Enter a sentence with an acronym: ")
sentence.split()
acronyms = []
for acronym in sentence.split():
    acronym_nu = acronym.translate(str.maketrans('','',string.punctuation))
    if len(acronym_nu) > 1:
        if acronym_nu.isupper():
            acronyms.append(acronym_nu)
print(acronyms)