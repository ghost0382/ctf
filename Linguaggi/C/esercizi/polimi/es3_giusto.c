#include <stdio.h>

int ppow(int);

int main(){
	
	int n;
	scanf("%d", &n);
	printf("%d", ppow(n));
	
}

int ppow(int n){
	
	int pow = 1;
	int tmp = pow + 2;

	for(int i = 0; i < n - 1; i++){
		pow += tmp;
		tmp += 2;
	}	
	
	return pow;
}
