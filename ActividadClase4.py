# Creo una lista llamada tareas
tareas = []

# Agregar al menos tres tareas distintas con insert() y diccionario
tareas.insert(0, {
    'nombre': 'Tarea 1',
    'descripcion': 'Descripción de la tarea 1',
    'estado': 'Completada'
})

tareas.insert(1, {
    'nombre': 'Tarea 2',
    'descripcion': 'Descripción de la tarea 2',
    'estado': 'Sin empezar'
})

tareas.insert(2, {
    'nombre': 'Tarea 3',
    'descripcion': 'Descripción de la tarea 3',
    'estado': 'En curso'
})

# Eliminar una tarea con pop()
tareas.pop(0)

# Mostrar las tareas restantes
print(tareas[0])
print(tareas[1])
