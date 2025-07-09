import string


def is_palindrome(str):
    for i in range(len(str) // 2 ):
        if str[i] != str[ -(i + 1)]:
            print('false')
            return False
    print('true')
    return True

def normalize(text):
    text = text.lower()
    text = text.replace("ï", "i").replace("é", "e").replace("è", "e").replace("ç", "c")
    text = text.translate(str.maketrans("", "", string.punctuation + string.whitespace + string.digits))
    text = ''.join(c for c in text if c.isalnum())
    print(text)
    return text

def is_text_palindrome(text):
    text = normalize(text)
    return is_palindrome(text)

is_text_palindrome("Esope reste ici et se repose")
is_text_palindrome("Engage le jeu que je le gagne ")
is_text_palindrome("La mère Gide digère mal")
is_text_palindrome("Eh ! ça va, la vache ?")
is_text_palindrome("Tu l'as trop écrasé, César, ce Port-Salut")
is_text_palindrome("Salut, comment ça va")
