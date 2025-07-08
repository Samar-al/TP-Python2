# créez une fonction qui prend en paramètres un **kwargs
# et qui renvoi la concaténation de toutes les clés valeur
# exemple function(je="suis", un="kwarg") doit renvoyer "jesuisunkwarg"
# exemple function(la="jolie", maison="dans", la="prairie") doit renvoyer "lajoliemaisondanslaprairie"

def concat(**kwargs):
    str = ""
    for key, value in kwargs.items():
        str += key + value
    print(str)
    return str

concat(je="suis", un="kwarg")
concat(la="jolie", maison="dans", prairie="verte")
concat(hello="world")