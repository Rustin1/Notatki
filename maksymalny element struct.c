#include <stdio.h>
#include <stdlib.h>

struct elem{
    int i;
    struct elem * next;
};

struct elem* dodaj(struct elem*Lista, int a){
    struct elem * wsk = malloc(sizeof(struct elem));
    wsk->i=a;
    wsk->next=Lista;
    return wsk;
};

struct elem* stworz(){
    return NULL;
};




struct elem * foo(struct elem* jeden, struct elem* dwa){
    struct elem* curr=jeden;
    struct elem* max =jeden;
    while(curr!=NULL){
        if(curr->i>max->i){
            max = curr;
        }
        curr=curr->next;
    }
    curr=dwa;
    while(curr!=NULL){
        if(curr->i>max->i){
            max = curr;
        }
        curr=curr->next;
    }
    return max;
}

int main()
{
    struct elem* element = stworz();
    struct elem* element2 = stworz();
    for(int i=1;i<11;i++){
        element = dodaj(element,i);
        element2 = dodaj(element2,i*4-10);
    }

    struct elem* max = foo(element,element2);

    printf("%d",max->i);

    return 0;
}
