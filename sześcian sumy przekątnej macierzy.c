include <stdio.h>
#include <stdlib.h>

int foo(int A, int B,int a[A][B])
{
	int min;
	if(A<B){
		min = A;
	}
	else{
		min = B;
	}
	int sum = 0;
	for(int x = 0;x < min;x++){
		sum += a[x][x]*a[x][x]*a[x][x];
	}
	return sum;
}

int main()
{
    int a[3][3]={
	{2,1,10},
	{1,2,1},
	{1,1,10}
	};
    printf("%d",foo(3,3,a));
    return 0;
}
