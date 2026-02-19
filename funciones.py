
import csv
from datos import usuarios, ids_registrados, campos
from validaciones import validar_entero, validar_email, input_no_vacio


def agregar_usuario():
    id_usuario = input_no_vacio("ID: ")

    if id_usuario in ids_registrados:
        print("ID ya existe")
        return

    nombre = input_no_vacio("Nombre: ")
    edad = validar_entero(input_no_vacio("Edad: "))

    if edad is None:
        print("Edad inválida")
        return

    email = input_no_vacio("Email: ")
    if not validar_email(email):
        print("Email inválido")
        return

    usuario = {
        "id": id_usuario,
        "nombre": nombre,
        "edad": edad,
        "email": email
    }

    usuarios.append(usuario)
    ids_registrados.add(id_usuario)
    print("Usuario agregado")


def listar_usuarios():
    if not usuarios:
        print("No hay usuarios registrados.")
        return
    for u in usuarios:
        print(f"{u['id']} | {u['nombre']} | {u['edad']} | {u['email']}")


def buscar_usuario():
    id_usuario = input_no_vacio("ID a buscar: ")
    for u in usuarios:
        if u["id"] == id_usuario:
            print(u)
            return
    print("No encontrado")


def eliminar_usuario():
    id_usuario = input_no_vacio("ID a eliminar: ")
    for u in usuarios:
        if u["id"] == id_usuario:
            usuarios.remove(u)
            ids_registrados.remove(id_usuario)
            print("Eliminado")
            return
    print("No encontrado")


def contar_usuarios_recursivo(lista):
    if not lista:
        return 0
    return 1 + contar_usuarios_recursivo(lista[1:])


def exportar_csv(nombre="usuarios.csv"):
    with open(nombre, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=campos)
        writer.writeheader()
        writer.writerows(usuarios)

    print("Archivo exportado")
