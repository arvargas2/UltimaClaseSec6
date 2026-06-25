usuarios_list = []  # BD


# ------- validaciones ----------------------
def validar_sexo(sexo):
    if sexo in ["M", "F"]:
        return True
    else:
        print("Error es valido F o M")
        return False


def validar_password(password):
    # que tenga min. 8 caracteres
    if len(password.strip()) < 8:
        print("Error min. 8 caracteres")
        return False

    tiene_numero = False
    for letra in password:
        if letra.isnumeric():
            tiene_numero = True

    tiene_letras = False
    for letra in password:
        if letra.isalpha():
            tiene_letras = True

    if " " in password:
        print("Error no puede tener espacios")
        return False

    return tiene_numero and tiene_letras


def imprimir_usuario(usuario):
    print(f"""
        --------------------------
        Nombre usuario: {usuario["nombre_usuario"]}
        Sexo: {usuario["sexo"]}  
        Password: {usuario["password"]} """)


# ------- transacciones ----------------------
