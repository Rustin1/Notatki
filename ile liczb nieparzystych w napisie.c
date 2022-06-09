#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int foo(char * napis){
	int dl = strlen(napis);
	int suma = 0;
	for(int i=0;i<strlen(napis);i++){
		char znak = napis[i];
		if(znak>=48&&znak<=57&&znak%2==1){
			suma += 1;
		}
	}
	return suma;
	
}

int main()
{
	char * napis = "koszojad53";
	printf("%d",foo(napis));
}
