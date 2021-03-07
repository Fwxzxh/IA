#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct nodo {
    char pal[20];
    struct nodo *sig;
} NODO;

NODO *inicio = NULL;

void alta(char *pal) {
    NODO *previo, *actual, *nuevo;
    previo = NULL;
    actual = inicio;
    while(actual && strcmp(actual->pal, pal) < 0) {
        previo = actual; 
        actual = actual->sig;
    }
    if(actual && !strcmp(actual->pal, pal)) {
        printf("La palabra %s ya existe\n", pal);
    } else {
        nuevo = (NODO *) malloc(sizeof(NODO));
        strcpy(nuevo->pal, pal);
        nuevo->sig = actual;
        if(previo) previo->sig = nuevo;
        else inicio = nuevo;
        printf("Se dio de alta: %s\n",pal);
    }
}

void reporte() {
    NODO *actual;
    actual = inicio;
    while(actual) {
        printf("%s\n",actual->pal);
        actual = actual->sig;
    }
}

void eliminaGral() {
    NODO *previo;
    while(inicio) {
        previo = inicio;
        inicio = inicio->sig;
        free(previo);
    }
}

void leeArchivo() {
    char palabra[20];
    FILE * fp;
    fp = fopen ("texto.txt", "w+");
    fscanf(fp, "%s", &palabra);
    printf("%s", palabra);
}

// una función para cargar del archivo
// una funcion que de de alta las palabras del archivo
// una función para sacar la probabilidad del achivo

int main() {
//    alta("casa");
//    alta("ventana");
//    alta("casa");
//    alta("puerta");
//    reporte();
//    eliminaGral();
    leeArchivo();
    return 0;
}