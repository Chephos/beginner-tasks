import pprint, string

def frequency_analysis(string):
    """Returns the frequency of a character in a string."""
    count = {}

    for character in string:
        if character.isspace():
            continue

        count.setdefault(character.lower(), 0)
        count[character.lower()] += 1

    return count



def frequency_analysis_word(strg):
    """Returns the frequency of a word in a string."""
    x = strg.split()
    count = {}

    for word in x:
        if word[-1] in string.punctuation:
            z = word[:-1]
            count.setdefault(z,0)
            count[z] += 1

        else:
            count.setdefault(word.lower(), 0)
            count[word.lower()] += 1

    return count


text = input('Enter a string: ')
pprint.pprint((frequency_analysis(text)))

test = "It is not good, is it good? bleh bleh bleh not bleh"
print(frequency_analysis_word(test))
 