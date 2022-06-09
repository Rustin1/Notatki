#include <stdio.h>
#include <stdlib.h>

struct node {
	int a;
	struct node * next;
};

struct node* dodaj(struct node*Lista, int i){
    struct node * wsk = malloc(sizeof(struct node));
    wsk->a=i;
    wsk->next=Lista;
    return wsk;
};

struct node* stworz(){
    return NULL;
};

void foo(struct node* tab){
    struct node* temp=tab;
    while(temp!=NULL){
        temp->a = temp->a*3;
        temp=temp->next;
    }
}

void wyswietlListeBezGlowy(struct node*Lista)
{
    struct node*temp=Lista;
    if(temp==NULL)
    {
        printf("Lista jest pusta\n");
    }
    while(temp!=NULL)
    {
        printf("%d\n",temp->a);
        temp=temp->next;
    }
    printf("----\n");
}

int main()
{
    struct node* tab = stworz();
    for(int i=1;i<11;i++){
        tab = dodaj(tab,i);
    }

    foo(tab);
    wyswietlListeBezGlowy(tab);

    return 0;
}
