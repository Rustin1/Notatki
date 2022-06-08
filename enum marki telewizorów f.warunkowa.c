#include <stdio.h>
#include <stdlib.h>

enum Telewizor{Samsung,LG,Apple};

int main()
{
    enum Telewizor tab[6] = {Samsung,Samsung,LG,LG,LG,Apple};
    for(int i=0;i<6;i++){
        if(tab[i]==0){
            printf("Samsung\n");
        }
    }
    return 0;
}
