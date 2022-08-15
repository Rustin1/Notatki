#include<stdio.h>
#include<stdlib.h>

int rek(int n){
	if(n==0){
		return -1; //start ciągu
	}
	else if(n==1){
                return -2;
        }
	return rek(n-1)+rek(n-2); //jeśli nie jest to wartość początkowa to zrob działanie (np +) na poprzedniej wartości z ciągu i liczbie (np 4 lub n)
}

int main(){
	printf("%d",rek(5));
	return 0;
}
