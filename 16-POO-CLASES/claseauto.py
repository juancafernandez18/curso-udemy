class Auto:
    patente="auto"
    marca="auto"
    color="auto"
    
    #constructor
    def __init__(self,patente,marca,color):
        self.patente = patente
        self.marca = marca
        self.color = color


    def setPatente(self,patente):
        self.patente=patente

    def getPatente(self):
        return self.patente

    def setMarca(self,marca):
        self.marca=marca
    def getMarca(self):
        return self.marca 
    def getColor(self):
        return self.color
    def setColor(self,color):
        self.color=color

    def MostrarAuto(self):
        
       info= "---- INFORMACION DEL AUTO---- "
       info += "\n"+"PATENTE MARCA COLOR"              
       
       
       info += " \n"+self.getMarca()+" "
       info +=self.getPatente()+" "
      
       info += self.getColor()+"\n"
      
       return info



