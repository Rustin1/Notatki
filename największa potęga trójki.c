#include <stdio.h>
#include <stdlib.h>

int foo(int n)
{
	int max = 0;
    for(int i=3;i<n;i=i*3){
    	max = i;
	}
	return max;
}

int main()
{
    printf("%d\n",foo(10));
    printf("%d\n",foo(27));
}
