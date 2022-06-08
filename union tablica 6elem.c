union XYZ{
   int a;
   char b;
};

int main(){
	union XYZ tab[6];
	tab[0].a = 1;
	tab[0].b = 'a';
	tab[1].a = 6;
	tab[1].b = 'b';
	tab[2].a = 2;
	tab[2].b = 'd';
	tab[3].a = 1;
	tab[3].b = 'q';
	tab[4].a = 8;
	tab[4].b = 'u';
	tab[5].a = 9;
	tab[5].b = 't';
	for(int i=0;i<6;i++){
		printf("%d,%c\n",tab[i].a,tab[i].b);
	}
	return 0;
}
