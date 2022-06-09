#include <stdio.h>
#include <stdlib.h>

struct element {
    float x;
    struct element  * next;
};

struct node* dodaj(struct node*Lista, float a){
    struct element * wsk = malloc(sizeof(struct element));
    wsk->x=a;
    wsk->next=Lista;
    return wsk;
};

struct element* stworz(){
    return NULL;
};

void wyswietlListeBezGlowy(struct element*Lista)
{
    struct element*tab=Lista;
    if(tab==NULL)
    {
        printf("Lista jest pusta\n");
    }
    while(tab!=NULL)
    {
        printf("%f\n",tab->x);
        tab=tab->next;
    }
    printf("----\n");
}

struct element * foo(struct element* tablica){
    return dodaj(tablica,100.45);;
}

int main()
{
    struct element* tablica = stworz();
    tablica = dodaj(tablica,10.5);
    tablica = dodaj(tablica,43.1);

    tablica = foo(tablica);
	wyswietlListeBezGlowy(tablica);
    
    return 0;
}
