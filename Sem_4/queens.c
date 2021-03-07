#include <stdio.h>

enum bool {FALSE, TRUE};
typedef enum bool boolean;

void ensayar(int i, boolean *q, int col[], boolean fila[], boolean diagb[], boolean diagc[]);

int main(void) {
    int i;
    boolean q;

    int col[8];
    boolean fila[8],diagb[15], diagc[15];

    for (i = 0; i < 8; i++) {
        fila[i] = TRUE;
    }
    for (i = 0; i < 15; i++) {
        diagb[i] = diagc[i] = TRUE;
    }

    ensayar(0, &q, col, fila, diagb, diagc);

    if (q) {
        printf("\nSolucion:");
        for (i = 0; i < 8; i++) {
            printf(" %d", col[i]);
        }
        printf("\n");
    }
    else {
        printf("\nNo hay solucion");
    }
    return 0;
}

void ensayar(int i, boolean *q, int col[], boolean fila[], boolean diagb[], boolean diagc[]) {
    int j;
    j = 0;
    *q = FALSE;
    do {
        if (fila[j] && diagb[i+j] && diagc[7+i-j]) {
            col[i] = j; fila[j] = diagb[i+j] = diagc[7+i-j] = FALSE;
            if (i < 7) { /* encuentra solucion? */
                ensayar(i+1, q, col, fila, diagb, diagc);
                if (!*q) {
                    fila[j] = diagb[i+j] = diagc[7+i-j] = TRUE;
                }
            }
            else {
                *q = TRUE; /* encuentra la solucion */
            }
        }
        j++;
    }
    while (!*q && j < 8);
}
