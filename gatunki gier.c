#include <stdio.h>
#include <stdlib.h>

enum gatunki{przygodowka,skradanka,RPG,strzelanka,strategia};

int main()
{
	enum gatunki gry[4] = {przygodowka,RPG,RPG,strzelanka};
	for(int i = 0;i<4;i++){
		if(gry[i]==2){
			printf("gra RPG\n");
		}
	}
}
