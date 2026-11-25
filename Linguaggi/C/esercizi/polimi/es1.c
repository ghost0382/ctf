// Questo esercizio richiede in input 3 valori interi e restituisce
// la sequenza di valori in ordine monotono crescente

#include <stdio.h>

int main(){
	
	int a, b, c, tmp;
	
	scanf("%d %d %d", &a, &b, &c);
	
	if(a > b){
		tmp = a;
		a = b;
		b = tmp;
	}
	
	if(b > c){
		tmp = b;
		b = c;
		c = tmp;
	}
	
	if(a > b){
		tmp = a;
		a = b;
		b = tmp;
	}
	
	printf("%d, %d, %d", a, b, c);
}
