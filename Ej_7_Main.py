from Ej_7_Bufe import LasBufes
from Ej_7_Alumno import Alumno
from Ej_7_Pedido import Pedido
from Ej_7_Plato import Plato

a = Alumno('ALU303','Pedro','Alfonsin','5')
a1 = Alumno('ALU303','Pedro','Raul','5')
Plato=Plato('PLA123','Pizza','145')
b = Pedido('123','12/12/12','si',Plato, a)
b1 = Pedido('124','11/11/11','si',Plato, a1)
Buf = LasBufes()
Buf.AgregarPedidos(b)
Buf.AgregarPedidos(b1)
Buf.GuardarPedidos()
Buf.GuardarPersonas()
Buf.GuardarPlatos()
Buf.Abrirlo()
print(Buf.Mostrar())