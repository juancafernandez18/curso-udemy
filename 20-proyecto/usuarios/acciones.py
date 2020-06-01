import usuarios.usuario as modelo

class Acciones:

    def registro(self,):
        print("\nOK, ah elegido registrarse..")
        print("------------------------------")
        nombre= input("Cual es tu nombre ?")
        apellido = input("Cual es tu apellido ?")
        email = input(" Cual es tu email ?")
        password = input("Ingresa una contraseña: ")

        usuario = modelo.Usuario(nombre,apellido,email,password)
        registro=usuario.registrar()

        if registro[0]>=1:
            print("-----------------------------------")
            print("Registrado correctamente el usuario: ",registro[1].nombre)
        else:
            print("No se ah podido registrar !")

        

    def login(self):
        print("\nOK, ah elegido loguearse en el sistema")
        print("------------------------------")
        try:
            email = input(" Cual es tu email ?")
            password = input("Ingresa una contraseña: ")

            usuario= modelo.Usuario("","",email,password)
            log= usuario.identificar()
            
            if email == log[3]:
                print("bienvenido! Te has registrado en el sistema")

        except Exception as e:
            print(type(e))
            print("Login Incorrecto, intenta de nuevo")


#agrego algo nuevo