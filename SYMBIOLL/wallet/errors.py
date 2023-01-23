from django.db import IntegrityError


class InsufficientBalance(IntegrityError):

    #Initialisation du paramètre message
    #A l'appel de la classe, obligation de
    #passer un paramètre de type chaîne de caractère

    def __init__(self, message: str):
        self.message = message

    def __str__(self):
        return self.message