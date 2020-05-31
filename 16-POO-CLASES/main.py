from claseauto import Auto

coche=Auto("nes822","mondeo","negro")

print(coche.MostrarAuto())

coche2=Auto("abc234","Gol","Negro Mate")

print(coche2.MostrarAuto())


print("----------------------------------------")
print("-----------Personas---------------------")

import persona

nuevapersona = persona.Persona("37885794","Juan","Fernandez","1000 viv")
print(nuevapersona.MostrarPersona())
print(nuevapersona.hablar())
print(nuevapersona.caminar())
print("----------Informatico------")
informatico= persona.Informatico()

informatico.setNombre("Juanca")
informatico.setApellido("Fernandez")
print(informatico.getNombre())
print(informatico.getLenguaje())
print(informatico.Programar())
print(informatico.RepararPC())
print(informatico.hablar())

print("------------Tecnico en redes------")
tecnico=persona.TecnicoRedes()
print(tecnico.Auditar())
tecnico.setNombre("Mi nombre es la red")
print(tecnico.getNombre())
print("lenguajes que hereda de informatico:",tecnico.getLenguaje())
