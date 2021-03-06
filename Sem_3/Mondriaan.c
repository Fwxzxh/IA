#include <stdio.h>
#include <stdlib.h>

int n;
int num = 1;
int ps = 1;

void imprime(int cuadricula[n][n]) {
    printf("%s", "Solución: ");
    printf("%d", num);
    printf("\n");
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            printf(" %0.2d ", cuadricula[i][j]);
        }
        printf("\n");
    }
}

void fill(int cuadricula[n][n], int x, int y, int p) {
    int r;
    if (cuadricula[x][y] == 0) {
        r = rand() % 100;
        if ((r % 2 == 0 && cuadricula[x+1][y] == 0) || (r % 2 == 0 && y == n-1)) {
            cuadricula[x][y] = p;
            cuadricula[x+1][y] = p;
            ps++;
        }
        else if (cuadricula[x][y+1] == 0 || x == n-1 ) {
            cuadricula[x][y] = p;
            cuadricula[x][y+1] = p;
            ps++;
        }
        else {
            fill(cuadricula, x, y, p);
        }
    }
}

void inicio() {
    int cuadricula[n][n];
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cuadricula[i][j] = 0;
        }
    }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            fill(cuadricula, i, j, ps);
        }
    }
    imprime(cuadricula);
}

int main() {
    printf("%s\n", "Ingrese el tamaño de la cuadricula");
    scanf("%d",&n);
    inicio();
    return 0;
}
