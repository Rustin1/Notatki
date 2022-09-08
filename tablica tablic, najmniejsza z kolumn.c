#include<stdio.h>
#include <stdlib.h>

int foo(int n, int m, int tab[n][m]){
	int minimum = tab[0][0];
	for(int x=0;x<n;x++){
		for(int y=0;y<m;y+=2){
			if(tab[x][y]<minimum){
				minimum = tab[x][y];
			}
		}
	}
	return minimum;
}

int main(){
	
	int tab[4][3] = {
	{2,3,-3},
	{1,4,7},
	{6,7,8},
	{-4,-10,7},
	};
	
	printf("%d",foo(4,3,tab));
	
	return 0;
}
