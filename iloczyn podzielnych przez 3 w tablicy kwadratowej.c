#include <stdio.h>
#include <stdlib.h>

int foo(int n, int tab[n][n]){
	int iloczyn = 1;
	for(int x=0;x<n;x++){
		for(int y=0;y<n;y++){
			if(tab[x][y]%3==0){
				iloczyn = iloczyn * tab[x][y];
			}
		}
	}
	return iloczyn;
}

int main()
{
	int tab[2][2] = {{3,2},{6,2}};
	printf("%d\n",foo(2,tab));
}
