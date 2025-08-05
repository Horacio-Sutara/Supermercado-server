from app.utils.consulta import consulta_general, consulta_por_condicion
# app/models/usuario.py
def obtener_usuarios():
    return consulta_general("usuario")
def obtener_usuario_por_id(usuario_id):
    return consulta_por_condicion("usuario", "id", usuario_id)
def obtener_usuario_por_email(email):
    return consulta_por_condicion("usuario", "email", email)
def obtener_usuario_por_nombre(nombre):
    return consulta_por_condicion("usuario", "nombre", nombre)
def obtener_usuario_por_telefono(telefono):
    return consulta_por_condicion("usuario", "telefono", telefono)  
def obtener_usuario_por_rol(rol):
    return consulta_por_condicion("usuario", "rol", rol)
def obtener_usuario_por_estado(estado):
    return consulta_por_condicion("usuario", "ACTIVO", estado)
def obtener_usuario_por_dni(dni):
    return consulta_por_condicion("usuario", "dni", dni)
def obtener_usuario_por_fecha(periodo, fecha):
    return consulta_por_condicion("usuario", f"DATE_PART(\'{periodo}\'),FECHA_REGISTRO", fecha)

if __name__ == "__main__":
    # Ejemplo de uso
    #usuarios = obtener_usuarios()
    usuarios= obtener_usuario_por_dni(45262093)
    print(usuarios)
