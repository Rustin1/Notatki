#include <stdio.h>
#include <stdlib.h>

struct Student{
	char * imie;
	int numer_albumu;
};

int foo(int n, struct Student tab[n]){
	int min = tab[0].numer_albumu;
	for(int i=1;i<n;i++){
		if(tab[i].numer_albumu < min){
			min = tab[i].numer_albumu;
		}
	}
	return min;
}

int main()
{
	struct Student tab[3];
	tab[0].imie = "Kuba";
	tab[1].imie = "Jakub";
	tab[2].imie = "Jakob";
	tab[0].numer_albumu = 5;
	tab[1].numer_albumu = 3;
	tab[2].numer_albumu = 8;
	printf("%d",foo(3,tab));
}
