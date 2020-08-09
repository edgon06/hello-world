#include <iostream>

using namespace std;

int main()
{
	/* Esto se añade para poder imprimir letras ñ y tildes sin problemas */
	setlocale(LC_CTYPE, "Spanish");
	
	cout<< "Hola Mundo" <<endl;
	printf("Hola Mundo");
	
	
}
