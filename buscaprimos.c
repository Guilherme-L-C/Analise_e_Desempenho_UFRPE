#include <stdio.h>
    // calculadora de raiz usando o método de newton
    double calcula_raiz(double n){
        
        if(n<0) return -1.0; 
        if(n==0) return 0; 
        
        double estimativa = n/2;
        double melhorEstimava; 

        for(int i =0; i <10; i++){
            melhorEstimava = 0.5 * (estimativa + (n / estimativa)); 
            estimativa = melhorEstimava; 
        }

        return estimativa; 
    }
    // calculo de numero primo
    int primo(int n){

        int d; 
        
        if(n <= 1) return 0; 
        if(n == 2) return 1; 
        if(n % 2 == 0) return 0;

        for(int d = 3; d*d <= n; d+=2){
            if(n % d == 0) 
                return 0; 
        }
        return 1;
    }
    // main
    int main(){
    
    double j; 
    int quantidadePrimo = 0;

    printf("Digite um numero: "); 
    if(scanf("%lf", &j)!= 1 || j <= 1){
        printf("Digite uma valor numerico > 1. ");
        return 1;
    }

    for(int i = 1; i <= (int)j; i++){
        if(primo(i)){
            if(quantidadePrimo > 0){
                printf("-");
            }
            printf("%d\n", i);
            quantidadePrimo++;
        }
    }

    printf("numero: %.2f, raiz: %.2f, quantidade de primos: %d", j, calcula_raiz(j), quantidadePrimo);

    return 0;  
}
