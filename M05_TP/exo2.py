#Anagramme
import string

def normalize(text):
    text = text.lower()
    text = text.replace("ï", "i").replace("é", "e").replace("è", "e").replace("ç", "c")
    text = text.translate(str.maketrans("", "", string.punctuation + string.whitespace + string.digits))
    text = ''.join(c for c in text if c.isalnum())
    return text

def is_anagramme(str1, str2):
    str1 = normalize(str1)
    str2 = normalize(str2)
    def letter_count(s):
        d = {}
        for char in s:
            if char.isalpha():
                d[char] = d.get(char, 0) + 1
        return d
    return letter_count(str1) == letter_count(str2)

print(is_anagramme('Albert Einstein','Rien n’est établi'))
print(is_anagramme('Léonard de Vinci','Créa le don divin'))
print(is_anagramme('cours python','python serpent'))