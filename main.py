import nubepalabras
import stack_usertags

while True:
    userid = input("Ingrese el id del usuario de stackoverflow en español para generar una nube de palabras con los tags mas usados o ingrese f para salir: ")

    if userid == "f" or userid == "F":
        break

    tags = stack_usertags.obtener_tags(userid)

    if tags == None:
        print("Error al ingresar el id")
    elif tags == "-1":
        print("El usuario no tiene etiquetas")
    else:
        nubepalabras.generar_imagen(tags, "Img/cloud_mask.png")

    

