
"""
Funciones de validación de entradas.
"""

import re

def validar_entero(valor):
    try:
        return int(valor)
    except ValueError:
        return None


def validar_email(email):
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(patron, email) is not None


def input_no_vacio(mensaje):
    while True:
        dato = input(mensaje).strip()
        if dato:
            return dato
        print("No puede estar vacío.")
