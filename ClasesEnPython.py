# =============================================================================
#       Clase
# =============================================================================
class MyClass:
    edad = 35 # atributo de clase

    def say_hi(self, msg): # método de clase
        return 'hello world' .format(msg)
    


# =============================================================================
#       Objeto, es una instanciación de una clase.
# =============================================================================


print(" \n \n  \t   ****************************  \t   Objeto  \t  ****************************  \n")
my_class = MyClass()
print(my_class)

print(" \n \n  \t   ****************************  \t   llamar al método de una clase  \t  ****************************  \n")

print(my_class.say_hi('tu'))



# =============================================================================
#       Argumento self
# =============================================================================


print(" \n \n  \t   ****************************  \t   Arugumento self, hace referencia al objeto instanciado  \t  ****************************  \n")

# ---------- start class ----------
class MiClase:
    name = "" # atributo de clase
    def __init__(self, name): # constructor
        self.name = name # atributo de instancia 
    
    def print_self(self):
        print(self)

    def return_self(self):
        return self
# ---------- end class  ----------

miClase1 = MiClase("Paco")
print(miClase1.name)
miClase2 = MiClase(name="Pepe")
print(miClase2.name)
#miClase1 is miClase1.return_self()


# =============================================================================
#      Visibilidad de los atributos
# =============================================================================

print(" \n \n  \t   ****************************  \t   Visibilidad de los atributos, protegidos y/o privados  \t  ****************************  \n")
class MyCar:
    _name_protected = "soy un atributo protegido"
    __name_private = "soy un atributo privado"

    def say_hi(self, msg):  #Método
        return 'hello world {}' .format(msg)
    


myCar1 = MyCar()
print("\n \n imprimir un método protegido \t myCar1._name_protected:  \t ", myCar1._name_protected)
# al ser un método privado no se puede acceder, nos da un error
#print(myCar1.__name_private)
#pero hay un "truco" y es poniendo objeto, punto, guión bajo, nombre de la clase, guión bajo, guión bajo y nombre del método
print("\n \n imprimir un método privado \t myCar1._MyCar__name_private:  \t ", myCar1._MyCar__name_private)



# =============================================================================
#      Getters and Setters
# =============================================================================


class GetterSetterClass:
    _mi_atributo_protegido = "This is a static variable"
    __mi_atributo_privado = "This is a static variable"

    def __init__(self, mi_atributo_protegido, mi_atributo_privado):
        self._mi_atributo_protegido = mi_atributo_protegido
        self.__mi_atributo_privado = mi_atributo_privado

    @property #get
    def mi_atributo_privado(self):
        return self.__mi_atributo_privado + " 2"
    
    @mi_atributo_privado.setter
    def mi_atributo_privado(self, value):
        self.__mi_atributo_privado = value + " 1"

claseGetterSetters = GetterSetterClass(mi_atributo_protegido="estoy protegido", mi_atributo_privado="soy privado")
claseGetterSetters.mi_atributo_privado = "soy una variable privada"
print("\n \n primero entra en el método 'setter' que tiene la anotación @mi_atributo_privado.setter  y después entra en el método 'get' que tiene la anotación @property \t claseGetterSetters.mi_atributo_privado:  \t ", claseGetterSetters.mi_atributo_privado)