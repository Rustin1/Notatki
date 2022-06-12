#include <stdio.h>
#include <stdlib.h>

int test(int a){
	return a*a;
}

int foo(int (*ptr)(int),int a){
	return ((*ptr)(a)%5);
}

int main()
{
	printf("%d",foo(&test,3));
}
