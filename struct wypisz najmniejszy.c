#include <stdio.h>
#include <stdlib.h>

struct Samolot {
	char * model;
	int liczba_silnikow;
};

struct Samolot foo(int n,struct Samolot Samoloty[n]){
	struct Samolot best;
	best = Samoloty[0];
	int min = Samoloty[0].liczba_silnikow;
	for(int i=1;i<n;i++){
		if(min > Samoloty[i].liczba_silnikow){
			min = Samoloty[i].liczba_silnikow;
			best = Samoloty[i];
		}
	}
	return best;
}

int main()
{
	struct Samolot Samoloty[5];
	Samoloty[0].liczba_silnikow = 5;
	Samoloty[1].liczba_silnikow = 2;
	Samoloty[2].liczba_silnikow = 3;
	Samoloty[3].liczba_silnikow = 7;
	Samoloty[4].liczba_silnikow = 1;
	Samoloty[0].model = "A320";
	Samoloty[1].model = "A321";
	Samoloty[2].model = "A322";
	Samoloty[3].model = "A323";
	Samoloty[4].model = "A324";
	struct Samolot best = foo(5,Samoloty);
	printf("%s\n",best.model);
}
