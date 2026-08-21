from vehicle import Vehicle

car = Vehicle()
print(car)

car1 = Vehicle('mazda')
print(car1)
car2 = Vehicle('Citroen','C3', 'rojo', 1.6)
print(car2)
car3 = Vehicle('Subaru', 'Legacy', 'azul', 3.0,  50.00)
print(car3)
car4 = Vehicle('mazda',  34.00)
print(car4)
car5 = Vehicle('mazda', '3', None, None,  34.00)
print(car5)

car6 = Vehicle(manufacturer='Nissan', color='grey')
print(car6)
car7 = Vehicle(manufacturer='Nissan', color='grey', cylinder=2.0)
print(car7)
car8 = Vehicle(manufacturer='Nissan', color='grey', cylinder=2.0)#, tu_vieja='en tanga') #TypeError: Invalid argument: tu_vieja
print(car8)

#por definicion cada objeto en python es unico, por lo que no se puede crear un objeto con los mismos argumentos
#para crear un objeto con los mismos argumentos, se debe usar el metodo __eq__
#__eq__ es un metodo especial en python que se usa para comparar objetos

