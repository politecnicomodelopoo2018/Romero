class Persona(object):
    Nombre=None
    Apellido=None
    ID = None

    def __init__(self,id,n,a):
        self.Nombre=n
        self.Apellido=a
        self.ID=id
    def Desc(self):
        return 0

    def getString(self):
        return self.__class__.__name__ + '|' + self.persona.ID + '|' + a.persona.Nombre + '|' + a.persona.Apellido + '|' + a.persona.Division + '\n'