
import funciones
from datos import usuarios


def menu():
    opciones = {
        "1": funciones.agregar_usuario,
        "2": funciones.listar_usuarios,
        "3": funciones.buscar_usuario,
        "4": funciones.eliminar_usuario,
        "5": lambda: print("Total de usuarios:", funciones.contar_usuarios_recursivo(usuarios)),
        "6": funciones.exportar_csv,
    }

    while True:
        print("""
===== SISTEMA DE GESTIÓN =====
1. Agregar usuario
2. Listar usuarios
3. Buscar usuario
4. Eliminar usuario
5. Contar usuarios
6. Exportar CSV
0. Salir
""")

        opcion = input("Opción: ")
        if not opcion:
            continue

        if opcion == "0":
            break
        
        accion = opciones.get(opcion)
        if accion:
            accion()
        else:
            print("Opción inválida")


if __name__ == "__main__":
    menu()
