#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Film {
    char * tytul;
	double ocena;
};

int foo(int n,struct Film Filmy[n]){
	int max = 0;
	for(int i=0;i<n;i++){
		if(max < strlen(Filmy[i].tytul)){
			max = strlen(Filmy[i].tytul);
		}
	}
	return max;
}
int main()
{
	struct Film Film[5];
	Film[0].tytul= "Forrest Gump";
	Film[1].tytul = "Spiderman";
	Film[2].tytul = "Morbius";
	Film[3].tytul = "Batman";
	Film[4].tytul = "Superman";
	Film[0].ocena = 7;
	Film[1].ocena = 6;
	Film[2].ocena = 9;
	Film[3].ocena = 2;
	Film[4].ocena = 5;
	printf("%d\n",foo(5,Film));
}
