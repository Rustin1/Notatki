#include <stdio.h>
#include <stdlib.h>

int *  foo(char* n){
	int dl = strlen(n)/2;
	if(strlen(n)%2 == 1){
		dl++;
	}
	static char ret[10];
	int x = 0;
	for(int i=0;i<strlen(n);i+=2){
		ret[x] = n[i];
		x++;
	}
	//printf("%s",ret);
	return ret;
}

int main()
{
    char h[] = "hadsfgj";
    //printf("%s",h);
    char* x;
    x = foo(h);
    printf("%s",x);
    return 0;
}
