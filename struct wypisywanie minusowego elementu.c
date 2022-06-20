#include <stdio.h>
#include <stdlib.h>

struct node{
    int t;
    struct node * next;
};

struct node* dodaj(struct node*Lista, int a){
    struct node * wsk = malloc(sizeof(struct node));
    wsk->t=a;
    wsk->next=Lista;
    return wsk;
};

struct node* stworz(){
    return NULL;
};

struct node * foo(struct node* tablica){
    struct node* wsk=tablica;
    while(wsk!=NULL){
        if(wsk->t<0){
            return wsk;
        }
        wsk=wsk->next;
    }
    
    return NULL;
}

int main()
{
    struct node* tablica = stworz();
    tablica = dodaj(tablica,5);
    tablica = dodaj(tablica,4);
    tablica = dodaj(tablica,-6);
    tablica = dodaj(tablica,7);
    tablica = dodaj(tablica,1);

    struct node* wynik = foo(tablica);
	
	if(wynik != NULL){
		printf("%d",wynik->t);
	}
	else{
		printf("brak minusowego elementu");
	}
    
    return 0;
}
