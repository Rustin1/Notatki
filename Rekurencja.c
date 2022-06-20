#include<stdio.h>
#include<stdlib.h>

int rek(n){
	if(n==0){
		return 4; //start ciągu
	}
	else if(n==1){
                return 5;
        }
	return rek(n-1)+4; //jeśli nie jest to wartość początkowa to zrob działanie (np +) na poprzedniej wartości z ciągu i liczbie (np 4 lub n)
}

int main(){
	printf("%d",rek(5));
	return 0;
}
