class Persona:
    __dni=""
    __nombre=""
    __apellido=""
    __direccion=""

    #constructor
    def __init__(self,dni,nombre,apellido,direccion):
        self.__dni=dni
        self.__nombre=nombre
        self.__apellido=apellido
        self.__direccion=direccion

    #getters y setters

    def getDni(self):
        return self.__dni

    def setDni(self,dni):
        self.__dni=dni

    def getNombre(self):
        return self.__nombre

    def setNombre(self,nombre):
        self.__nombre= nombre
    
    def getApellido(self):
        return self.__apellido

    def setApellido(self,apellido):
        self.__apellido=apellido

    def getDireccion(self):
        return self.__direccion

    def setDireccion(self,direccion):
        self.__direccion= direccion
    
    def MostrarPersona(self):
        print("Dni: ",self.getDni())
        print("Nombre: ",self.getNombre())
        print("Apellido: ",self.getApellido())
        print("Direccion: ",self.getDireccion())

    def hablar(self):
        return "Hola estoy hablando"
    def caminar(self):
        return "Voy caminando"

class Informatico(Persona):
    __lenguajes=""
    __experiencia=""

    def __init__(self):
        self.__lenguajes= "Python html5"
        self.__experiencia= 5

    def getLenguaje(self):
        return self.__lenguajes
    def setLenguaje(self,lenguaje):
        self.__lenguajes=lenguaje

    def getExperiencia(self):
        return self.__experiencia
    def setExperiencia(self,experiencia):
        self.__experiencia = experiencia

    def Programar(self):
        return "Estoy programando"

    def RepararPC(self):
        return "Reparo pc y telefonos"

class TecnicoRedes(Informatico):
    def __init__(self):
        super().__init__()
        self.auditoria= "Experto"
        self.experienciaRedes = 15
    
    def Auditar(self):
        return "Estoy haciendo una auditoria en la red"
