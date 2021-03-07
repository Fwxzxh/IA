#include <stdlib.h>
#include <stdio.h>

int n;
int sol = 1;
const int ejex[8] = {-1,-2,-2,-1, 1, 2, 2, 1},
          ejey[8] = {-2,-1, 1, 2, 2, 1,-1,-2};

void imprimir(int tablero[n][n], int sol) {
    printf("%s","Solucion: ");
    printf("%d",sol);
    printf("\n");
    for (int i=0; i<n; i++) {
        for (int j=0; j<n; j++) {
            printf(" %0.2d ",tablero[i][j]);
        }
        printf("\n");
    }
}

void mover(int tablero[n][n], int i, int pos_x, int pos_y) {
    int k, u, v;
    int ncuad = n*n;
    for (k = 0; k < 8; k++) {
        u = pos_x + ejex[k];
        v = pos_y + ejey[k];
        if (u >= 0 && u < n && v >= 0 && v < n) { // esta dento?
            if (tablero[u][v] == 0) {
                tablero[u][v] = i;
                if (i < ncuad) {
                    mover(tablero, i+1, u, v);
                }
                else {
                    imprimir(tablero, sol++);
                }
                tablero[u][v] = 0;
            }
        }
    }
}

void inicio(int n, int x, int y) {
    int tablero[n][n];
    for (int i=0; i<n; i++) {
        for (int j=0; j<n; j++) {
            tablero[i][j]=0;
        }
    }
    tablero[x][y] = 1;
    mover(tablero,2,0,0);
}

int main () {
    int x,y;
    printf("%s\n", "Ingrese el tamaño del tablero");
    scanf("%d",&n);
    printf("%s\n", "Ingrese las cordenadas de inicio del caballo (Ej. 0,0)");
    scanf("%d,%d",&x,&y);
    inicio(n, x, y);
    return 0;
}
