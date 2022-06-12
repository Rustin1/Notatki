#include <stdio.h>
#include <stdlib.h>

enum Telewizor{fullHD,a4k,a8k};

int main()
{
	enum Telewizor TV[6] = {
		fullHD,fullHD,a4k,a8k,a4k,a8k
	};
	for(int i=0;i<6;i++)
    {
        if(TV[i]==1){
        	printf("telewizor w wysokiej jakosci 4k\n");
		}
    }
}
