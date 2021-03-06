/* latino.c */

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int n, *a, *b, total, p;

void inicializa() {
    // pide n, guarda los espacios necesarios para la matriz en a, pone contadores a 0
    printf("n: "); scanf("%d",&n);
    a = (int *) malloc(sizeof(int) * n * n);
    b = (int *) malloc(sizeof(int) * n * n);
    total = 0; p = 0;
}

int posic(int r, int c) {
    return r * n + c;
}

void reverse() {
    int i, j;
    for (i = p-1, j = 0; i >= 0 ; i--, j++)
        b[j] = a[i];
}

void imprime() {
    int i, j;
    reverse();
    printf("Solucion: %d\n", ++total);
    for(i=0; i<n; ++i) {
        for(j=0; j<n; ++j) printf("   %c, %lc", 64 + a[posic(i,j)], 96 + b[posic(i,j)]);
        printf("\n");
    }
    printf("\n");
}

int noRepiteRen(int valor) {
    int columna, i;
    columna = p % n;
    for(i=0; i<p/n; ++i)
        if(a[posic(i,columna)] == valor) return 0;
    return 1;
}

int noRepiteCol(int valor) {
    int renglon, i;
    renglon = p / n;
    for(i=0; i<p%n; ++i)
        if(a[posic(renglon,i)] == valor) return 0;
    return 1;
}

void resuelve() {
    int i;
    for(i=1; i<=n; ++i)
        if(noRepiteRen(i) && noRepiteCol(i)) {
            a[p++] = i;
            if(p == n*n) imprime();
            else resuelve();
            --p;
        }
}


int main() {
    time_t inicio, fin;
    inicializa();
    inicio = time(NULL);
    resuelve();
    free(a);
    fin = time(NULL);
    printf("Tiempo de procesamiento: %ld seg\n",fin-inicio);
    return 0;
}
