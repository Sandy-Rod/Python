import dis
import itertools
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
#       Slicing, clave : valor
# =============================================================================

print(" \n \n  \t   ****************************  \t    SLICING  \t  ****************************  \n")
print("secuencia[inicio:fin:paso]")
texto = "hola Mundo"

print(texto[:4])    # primeros 4 caracteres
print(texto[-5:])   # últimos 5 caracteres
print(texto[1::2])  # posicion impares
print(texto[::-1])   # posicion impares




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






print(" \n \n ------- Tipos de listas comprimidas ------------ \n ")

print(" \n \t type([i for i in range(4)])")
print(type([i for i in range(4)]))

print(" \n \t type((i for i in range(4)))")
print(type((i for i in range(4))))

print(" \n \t type(tuple(i for i in range(4)))")
print(type(tuple(i for i in range(4))))

print(" \n \t type({i for i in range(4)})")
print(type({i for i in range(4)}))

print(" \n \t type({i:i for i in range(4)})")
print(type({i:i for i in range(4)}))





# =============================================================================
#       FUNCIONES CON LISTAS COMPRIMIDAS
# =============================================================================

print(" \n \n  \t   ****************************  \t    Range, un clásico  \t  ****************************  \n")
print("range(4)")
print(range(4))


print("\n Hay que pasar una lista para que el generador se ejecute y podamos recuperar sus valores --> \t listrange(4) ")
print(list(range(4)))

print(" \n \n  \t   ****************************  \t    Map  \t  ****************************  \n")
print("list(map(lambda x: x/2, (i for i in range(10))))")
print( list(map(lambda x: x/2, (i for i in range(10)))))


print(" \n \n  \t   ****************************  \t    Filter \t  ****************************  \n")
print("list(filter(lambda x: x%2, (i for i in range(10))))")
print( list(filter(lambda x: x%2, (i for i in range(10))))) 




print(" \n \n  \t   ****************************  \t    All and Any \t  ****************************  \n")
print("el resultado es false porque no todos los elementos de la lista son True -->  \t all([True, False, True, True]) ")
print( all([True, False, True, True]))

print("\n \n el resultado es True porque todos los elementos de la lista son True -->  \t all([True, True, True, True]) ")
print( all([True, True, True, True]))

print("\n \n el resultado es True porque uno de los elementos de la lista es True -->  \t any([False, True, False, False]) ")
print( any([False, True, False, False]))


print("\n \n el resultado es False porque ningun elemento de la lista es True -->  \t any([False, False, False, False]) ")
print( any([False, False, False, False]))


print(" \n \n  \t   ****************************  \t    Itertools  \t  ****************************  \n")
print(" podemos acumular suma de elementos de una lista con accumulate -->  \t  list(itertools.accumulate(i for i in range(5))) ")
print(list(itertools.accumulate(i for i in range(5))))

print("\n \n  hazme el producto de esta lista -ABCD- pudiendo repetir dos elementos, nos devuelve una tupla de dos elementos --> \t  list(itertools.product('ABCD', repeat=2)) ")
print(list(itertools.product('ABCD', repeat=2)))


print("\n \n sobre la funcion interior, iteramos la tupla anterior descriminando los que son iguales  [(p1, p2) for p1, p2 in itertools.product('ABCD', repeat=2) if p1 != p2 ] ")
print([(p1, p2) for p1, p2 in itertools.product('ABCD', repeat=2) if p1 != p2 ])



# =============================================================================
#       GENERADORES, los generadores son funciones que devuelven un iterador, nos permiten crear una lista de manera dinámica
# =============================================================================
print(" \n \n  \t   ****************************  \t   Función generador  \t  ****************************  \n")
def interfunc():
    for i in range(5):
        yield i

print("creando una lista llamand una función generador --> \t list(interfunc())")
print(list(interfunc()))



# =============================================================================
#       PROMISES, son coroutines, funciones con estado
# =============================================================================


print(" \n \n  \t   ****************************  \t   Thread  \t  ****************************  \n")
import time

def countdown(number):
    while number > 1:
        number -= 1

if __name__ == "__main__":
    start = time.time()
    
    count = 10000000
    countdown(count)

    print(f"Tiempo de ejecución: {time.time() - start}")



