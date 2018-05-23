import json
class Persona(object):
    Nombre=None
    Apellido=None
    fecha_Nac=None

lista = []
caca=Persona()
caca.Nombre='pedro'
caca.Apellido='rodriguez'
caca.fecha_Nac='12/23/2018'

caca2=Persona()

caca2.Nombre='MELMAN'
caca2.Apellido='rodrigu,jh,hjgbez'
caca2.fecha_Nac='12/jgh23/2018'


#lista.append(caca)
#lista.append(caca2)
dicaca = {'personas':[]}

for a in lista:
    dicaca['personas'].append(
        {
            'nombre':a.Nombre,
            'apellido':a.Apellido,
            'nacimiento':a.fecha_Nac
        }
    )

#algo = json.dumps(dicaca)

#with open('JSON/caca','w') as f:
 #   f.write(algo)
print(lista)
with open('JSON/caca','r') as f:
    cacargados=f.read()

    algo=json.loads(cacargados)

    for a in algo["personas"]:

        caa = Persona()
        caa.Nombre=a["nombre"]
        caa.Apellido=a["apellido"]
        caa.fecha_Nac=a["nacimiento"]
        lista.append(caa)


print(lista[0].Nombre,lista[0].Apellido,lista[0].fecha_Nac)
print(lista[1].Nombre,lista[1].Apellido,lista[1].fecha_Nac)