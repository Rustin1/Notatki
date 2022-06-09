#include <stdio.h>
#include <stdlib.h>
#include <string.h>

const char *samogloski = "aeiouy";

int samogloska(char litera){
	for(int i = 0;i<strlen(samogloski);i++){
		if(litera == samogloski[i] || litera == samogloski[i]-97+65){
			if(litera>=65&&litera<=90||litera>=97&&litera<=122){
				return 1;
			}
		}
	}
	return 0;
}

int foo(char * napis){
	int dl = strlen(napis);
	int suma = 0;
	for(int i = 0;i<dl;i++){
		if(samogloska(napis[i]) == 0){
			suma += 1;
		}
	}
	return suma;
}

int main()
{
	char* napis = "Ala Ma Kota";
	printf("%d",foo(napis));
}
