#include <stdio.h>
#include <stdlib.h>

int foo(int n,int tab[n]){
	int sum = 0;
	for(int i = 0;i<n;i++){
		if(tab[i]<0){
			sum += tab[i];
		}
	}
	return sum;
}

int main()
{
	int tab[3] = {1,-4,-2};
	printf("%d",foo(3,tab));
}
