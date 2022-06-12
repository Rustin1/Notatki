#include <stdio.h>
#include <stdlib.h>

struct Pracownik{
	char * imie;
	int nr;
	float wynagrodzenie;
};

int foo(int n, struct Pracownik tab[]){
	float max = tab[0].wynagrodzenie;
	int maxnr = tab[0].nr;
	for(int i = 1;i<n;i++){
		if(tab[i].wynagrodzenie > max){
			max = tab[i].wynagrodzenie;
			maxnr = tab[i].nr;
		}
	}
	return maxnr;
}

int main()
{
	struct Pracownik tab[3];
	for(int i = 0; i < 3; i++){
		tab[i].nr = i;
		tab[i].wynagrodzenie = 4000 + 100*i;
	}
	tab[0].imie = "Konstantyn";
	tab[1].imie = "Konstantynopoli";
	tab[2].imie = "Konstantynopolitanczykowianeczka";
	printf("%d",foo(3,tab));
}
