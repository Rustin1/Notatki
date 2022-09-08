#include<stdio.h>
#include <stdlib.h>

int foo(char * n1, char * n2){
	int d1 = 0;
	int d2 = 0;
	int c1 = 0;
	int c2 = 0;
	for (int i = 0; n1[i] != '\0'; i++)
    {
        d1++;
        if(n1[i] > 47 && n1[i] < 58){
        	c1++;
		}
    }
    for (int i = 0; n2[i] != '\0'; i++)
    {
        d2++;
        if(n2[i] > 47 && n2[i] < 58){
        	c2++;
		}
    }
    if(d2>1){
    	return c1;
	}
	return c2;
}

int main(){
	
	char * n1 = "1230";
	char * n2 = "1234567890";
	
	printf("%d",foo(n1,n2));
	
	return 0;
}
