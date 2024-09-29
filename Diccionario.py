# Crear un diccionario llamado informacion_personal
informacion_personal = {
    "nombre": "Carlos Pérez",
    "edad": 30,
    "ciudad": "Quito",
    "profesion": "Ingeniero"
}

# Acceder al valor asociado con la clave "ciudad" y modificarlo
informacion_personal["ciudad"] = "Guayaquil"

# Agregar una nueva clave-valor al diccionario, en este caso "profesion"
informacion_personal["profesion"] = "Desarrollador de Software"

# Verificar si la clave "telefono" existe en el diccionario, si no, agregarla
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0991234567"

# Eliminar la clave "edad" del diccionario
informacion_personal.pop("edad")

# Imprimir el diccionario resultante
print("Diccionario Final:", informacion_personal)
