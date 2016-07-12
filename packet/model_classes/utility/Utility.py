from pump_app.models import *
import types

class Utility:
    class Meta:
		abstract = True

    #metodo per convertire una stringa in un nuovo oggetto il cui nome della classe coincide con
    #quello della stringa. Da usare con attenzione poiche' se eval fallisce causa un deep brake
    def str_to_class(self, s):
        instance = eval(s)()
        return instance