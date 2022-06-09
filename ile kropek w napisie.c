#include <stdio.h>
#include <stdlib.h>

int foo(char * napis){
	int size = sizeof(napis)/sizeof(napis[0]);
	int suma = 0;
	for(int i =0 ;i<size;i++){
		if(napis[i]=='.'){
			suma++;
		}
	}
	return suma;
}

int main()
{
	char * napis = "n.a.p.i.s";
	printf("%d",foo(napis));
}
