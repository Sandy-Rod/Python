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
print(myCar1._name_protected)
#print(myCar1.__name_private)


