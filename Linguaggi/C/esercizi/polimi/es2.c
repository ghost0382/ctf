// Questo programma richiede di inserire la lunghezza di una sequenza
// di interi e i rispettivi valori.
// Indica quindi il massimo valore e il suo indice

#include <stdio.h>

int main(){
	
	int seq, n, max_n, max_i = 1;
	
	do{
		printf("Enter sequence length: ");
		scanf("%d", &seq);
	}while(seq <= 0);
	
	printf("1 su %d numero: ", seq);
	scanf("%d", &max_n);
	
	for(int i = 1; i < seq; i++){
		printf("%d su %d numero: ", i + 1, seq);
		scanf("%d", &n);
		if(n >= max_n){
			max_n = n;
			max_i = i + 1;
		}
	}
	
	printf("max_n: %d\nmax_i: %d", max_n, max_i);
	
	return 0;
}

