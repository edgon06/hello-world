#Ejemplo de funciones

def imprimir():
 mensaje = input("Introduce un mensaje para mostrar: ")    
 print("el mensaje es: ", mensaje)
 numero = int(input("Introduce un numero para mostrar: "))
 print("el numero es: ", numero)

#Llamado a una función
imprimir()

#Python en lugar de indicar que elementos pertenecen a una funcion a traves de llaves o corchetes 
#utiliza tabulado, por ello, es muy importante mantener un codigo bien estructurado

#Las variables no necesitan declararse, el interprete de python asume su tipo cuando se les asigna un valor
#Por lo anterior, es necesario hacer cast a los valores introducidos en una variable

#En general, los programas en python no tienen una funcion "main()", pues su funcionamiento es similar a un script
# Sin embargo, si un programa se quiere poder ser usado tanto como una importación (sin ejecutar sus funciones directamente), 
# como de forma independiente como programa principal,
# se puede hacer lo siguiente:

if __name__ == "__main__":
    print('Ejecutando como programa principal (desde el <<main>>)')
    imprimir() 

# Esto se debe a que durante la ejecución, el interprete le da a todo archivo un atributo __name__ 
# si tienes un archivo llamado mi_modulo.py, si lo ejecutamos como 
# programa principal el atributo __name__ será '__main__', 
# si lo usamos importandolo desde otro modulo (import mi_modulo) 
# el atributo __name__ será igual a 'mi_modulo'.
# El interprete le da al archivo actualmente ejecutando el valor "__main__" al atributo __name__ del archivo