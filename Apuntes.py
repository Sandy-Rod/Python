import dis

# =============================================================================
#       Listas  
# =============================================================================
lista = [1, 2, 3]
print(" \n \n  \t   ****************************  \t  MÉTODOS DE LISTA \t  ****************************  \n")
print(dir(list))

# =============================================================================
#       Tuple, son inmutables, una vez definidas no se puede alterar
# =============================================================================
tupla = (1, 2, 3)
print(" \n \n  \t   ****************************  \t  MÉTODOS DE TUPLA, una vez definidas no se puede alterar \t  ****************************  \n")
print(dir(type(tuple)))

# =============================================================================
#       SET, el contenido debe ser elementos no repetidos e inmutables, no garantiza la ordenación.
# =============================================================================
conjuto = {1, 2, 3}
print(" \n \n  \t   ****************************  \t  MÉTODOS DE SET, el contenido debe ser elementos no repetidos e inmutables, no garantiza la ordenación. \t  ****************************  \n") 
print(dir(list))

# =============================================================================
#       DICCIONARIO, clave : valor
# =============================================================================

diccionario = {"primerElemento_Clave1":"primerElemento_Valor1",
               "primerElemento_Clave2":"primerElemento_Valor3",
               "primerElemento_Clave3":"primerElemento_Valor3"
               }
print(" \n \n  \t   ****************************  \t  DICCIONARIO, clave : valor \t  ****************************  \n") 
print(diccionario)
print(dir(diccionario))



# =============================================================================
#       BYTECODE, 
# =============================================================================

def my_function(num):
    result = []
    for i in range(num):
        result.append(i)
    return result
print(" \n \n  \t   ****************************  \t  BYTECODE, una funcion que itera las veces del número que le pasamos y agrega un valor a una lista. con dis.dis vemos que pasa por debajo  \t  ****************************  \n") 
dis.dis(my_function)

print("\n \n nombres de variables que hay en mi función \t my_function.__code__.co_varnames:  \t ", my_function.__code__.co_varnames)
print("\n \n funciones de python que utilizo en mi función \t my_function.__code__.co_names:  \t ", my_function.__code__.co_names)
print("\n \n en qué linea empieza mi función \t my_function.__code__.co_firstlineno:  \t ", my_function.__code__.co_firstlineno)
print("\n \n my_function.__code__.co_name:  \t ", my_function.__code__.co_name)
print("\n \n my_function.__code__.co_code:  \t ", my_function.__code__.co_code)


# =============================================================================
#       LIST COMPREHENSION
# =============================================================================

print(" \n \n  \t   ****************************  \t    LIST COMPREHENSION  \t  ****************************  \n") 

[i for i in range(10)]
print("creación de una lista: \t ", [i for i in range(10)])
print("\n \n recorrer una lista y sumar el elemento consigo mismo: \t ", [i + i for i in (1,2,3,4)])

print("\n \n recorrer una lista y añadir condicional \t ", [i for i in (1,2,3,4) if i != 2])
print("\n \n for dentro de un for, como resultado creamos una tupla : \t ", [(i,j) for i in (1,2,3) for j in (4,5,6)])
print("\n \n con tres bucles, como resultado creamos una tupla de tres elementos : \t ", [(i,j,k) for i in (1,2,3) for j in (4,5,6) for k in (7,9)])

print("\n \n función con listas comrpimidas \n ")
def say_hello(i):
    return (f"hola {str(i)}")
print([say_hello(i) for i in (1,2,3,4,5)])





print("\n \n ------- Tipos de listas comprimidas: \n ")
print("\n \ttype([i for i in range(4)])")
print(type([i for i in range(4)]))
print("\n \t type((i for i in range(4)))")
print(type((i for i in range(4))))
print("\n \t type(tuple(i for i in range(4)))")
print(type(tuple(i for i in range(4))))
print("\n \t type({i for i in range(4)})")
print(type({i for i in range(4)}))
print(" \n \t type({i:i for i in range(4)})")
print(type({i:i for i in range(4)}))