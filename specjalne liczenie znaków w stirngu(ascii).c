#include <stdio.h>
#include <stdlib.h>

int foo(char a[], char b[], int n)
{
	int rozmiarA = sizeof(a)/sizeof(a[0])-1;
	int rozmiarB = sizeof(b)/sizeof(b[0])-1;
	if(rozmiarA < n || rozmiarB < n){
		return 0;
	}
    if(a[n] < b[n]){
    	return 1;
	}
	return 0;
}

int main()
{
    char a[] = "haha";
    char b[] = "zzz";
    printf("%d",foo(a,b,2));
    return 0;
}
