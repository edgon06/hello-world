import os

#metodo para generar una funcion en un nuevo archivo py que simule el funcionamiento de un hecho de prolog
def assertz(hecho,num_arg):
    #hay que buscar una forma de saber el numeros de hechos de un mismo tipo que existen
    num_hechos=0
    declaracion_de_hecho = "def "+hecho+"("
    n_predicado = 0
    for n_predicado in range(1,num_arg):
        predicado = "a" + str(n_predicado)
        declaracion_de_hecho = declaracion_de_hecho + predicado
        lista_de_predicados[n_predicado] =  hecho+"["+str(num_hechos)+"]["+str(n_predicado)+"]="+ predicado
        if n_predicado < num_arg:
            declaracion_de_hecho = declaracion_de_hecho +","
        else:
            declaracion_de_hecho = declaracion_de_hecho +"):"+ os.linesep

    file = open("C:/hechos.py","w")
    file.write(declaracion_de_hecho) #hacer el calculo de las tabulaciones de la funcion
    for i in range(1,num_arg):
        file.write(lista_de_predicados[i] + os.linesep)
    file.write("")
    #hacer que dependiendo de si los  valores de los algoritmos argumentos de la funcion estan en mayuscula, asignarlos a una lista e 
    #imprimirlos por pantalla o retornar la lista
    file.close()
    





if __name__ == "__main__":
