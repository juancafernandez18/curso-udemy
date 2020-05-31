import os

#crar carpeta

if not os.path.isdir("./mi_carpeta"):
    os.mkdir("./mi_carpeta")
else:
    print("la carpeta ya existe")

#borrar carpeta

# os.rmdir("./mi_carpeta")

