// Questo programma individua tutti i numeri primi in un range da 0 a n.
//	[FUNZIONE]	isPrime		: return 1 se e' prime, 0 se non e' prime
//	[FUNZIONE]	primeSeq	: stampa a video la sequenza di numeri primi
//								dato un valore

#include <stdio.h>
#include <stdbool.h>

int isPrime(int);
void primeSeq(int);

int main(){

	int n;
	
	printf("  > Inserisci il numero: ");
	scanf("%d", &n);
	primeSeq(n);
	
}

int isPrime(int n){
	
	int div = 3;
	
	if(n < 2) return 0;
	if(n == 2) return 1;
	if(n % 2 == 0) return 0;

	while(div <= n / div){
		if(n % div == 0)
			return 0;
		div += 2;
	}
	return 1;
}

void primeSeq(int n){
    printf("\n\n ------ Sequenza ------- \n\n");

    for (int j = 0, i = 2; i <= n; i += (i == 2 ? 1 : 2))
        if (isPrime(i)) {
            printf("%3d ", i);
            if (++j % 5 == 0) printf("\n");
        }
}




