from app.utils.consulta import consulta_general, consulta_por_condicion
from app.utils.insert import insertar_datos
from app.utils.update import actualizar_datos

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

def insertar_usuario(nombre, apellido, dni, contraseña, correo,rol="USER",activo=True,telefono=None):
    entidad = "usuario"
    columnas = "nombre, apellido, dni, telefono, rol, activo, contraseña, correo"
    valores = (nombre, apellido, dni, telefono, rol, activo, contraseña, correo)
    insertar_datos(entidad, columnas, valores)
    print("Usuario insertado con éxito.")

def actualizar_id_usuario(condicion,nuevo_id):
    entidad = "usuario"
    columnas = ["id"]
    valores = (nuevo_id)
    condicion= f"id = {condicion}"
    print(condicion)
    actualizar_datos(entidad, columnas, valores, condicion)
    print("Usuario actualizado con éxito.")




if __name__ == "__main__":
    # Ejemplo de uso
    actualizar_id_usuario(7,"3")
    usuarios = obtener_usuarios()
    #usuarios= obtener_usuario_por_dni(45262093)
    #insertar_usuario("Pedro", "Gómez", 11111111, "admin123","user@gmail.com", "USER", True, "1234567891")
    print(usuarios)
