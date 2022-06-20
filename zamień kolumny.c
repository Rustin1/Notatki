#include <stdio.h>
#include <stdlib.h>

int * foo(int n, int m,int tab[n][m]){
	for(int x=0;x<n;x++){
		for(int y=0;y<m/2;y++){
			int tym = tab[x][y];
			tab[x][y] = tab[x][m-y-1];
			tab[x][m-y-1] = tym;
		}
	}
	return tab;
}

int main()
{
	int n = 4;
	int m = 5;
	int tab[4][5]={
	{1,2,3,4,5},
	{1,2,3,4,5},
	{7,4,6,2,4},
	{6,2,4,2,5}
	};
	int *nowa;
	nowa = foo(n,m,tab);
	for(int i=0;i<n*m;i++){
		printf("%d ",nowa[i]);
		if((i+1)%m==0){
			printf("\n");
		}
	}
    return 0;
}
