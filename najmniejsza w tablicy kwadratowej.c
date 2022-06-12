#include <stdio.h>
#include <stdlib.h>

int foo(int n, int ** tab)
{
	int miny = 0;
	int min = tab[0][0];
	for(int x=0;x<n;x++){
		for(int y=0;y<n;y++){
			if(tab[x][y]<min){
				min=tab[x][y];
				miny = y;
			}
		}
	}
	return miny;
}

int **rezerwacja(int n, int m)
{
    int **tab=(int**)malloc(sizeof(int*)*n);
    for(int i=0;i<n;i++)
    {
        *(tab+i)=(int*)malloc(sizeof(int)*m);
    }
    return tab;
}

int main()
{
	int **tab = rezerwacja(3,3);
	for(int i=0;i<3;i++)
    {
        for(int j=0;j<3;j++)
        {
            tab[i][j]=i*-j;
        }
    }
	printf("%d",foo(3,tab));
}
